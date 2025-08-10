"""
Moduł obsługujący trasy Trakera wydatków
"""

from datetime import datetime

from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)

import re
from flask import make_response
from sqlalchemy.exc import SQLAlchemyError
from app.models import db, User, Expense

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Zaloguj się, aby uzyskać dostęp do tej strony"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    """Wczytuje użytkownika na podstawie ID z bazy danych"""
    return db.session.get(User, int(user_id))


def handle_expense_form(form_data):
    """Obsługuje tworzenie nowego obiektu Expense na podstawie danych z formularza"""
    amount = float(form_data["amount"])
    description = form_data["description"]
    category = form_data["category"]
    date_value = datetime.strptime(form_data["date"], "%Y-%m-%d").date()

    return Expense(
        amount=amount,
        description=description,
        category=category,
        date=date_value,
        user_id=current_user.id,
    )


def init_routes(app):
    """Rejestruje trasy aplikacji"""
    register_auth_routes(app)
    register_expense_routes(app)


def register_auth_routes(app):
    """Trasy logowania, rejestracji i wylogowania"""

    @app.route("/register", methods=["GET", "POST"])
    def register():
        """Rejestracja nowego użytkownika"""
        if request.method == "POST":
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]

            if len(password) < 8:
                flash("Hasło musi mieć co najmniej 8 znaków", "danger")
                return redirect(url_for("register"))

            if not re.search(r"\d", password):
                flash("Hasło musi zawierać co najmniej jedną cyfrę", "danger")
                return redirect(url_for("register"))

            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, email):
                flash("Podaj poprawny adres email", "danger")
                return redirect(url_for("register"))

            existing_user = User.query.filter(
                (User.username == username) | (User.email == email)
            ).first()
            if existing_user:
                flash("Użytkownik lub email już istnieje", "danger")
                return redirect(url_for("register"))

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash("Rejestracja zakończona sukcesem", "success")
            return redirect(url_for("login"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        """Logowanie użytkownika"""
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            remember = "remember" in request.form

            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user, remember=remember)
                flash("Zalogowano!", "success")
                return redirect(url_for("index"))

            flash("Nieprawidłowy login lub hasło", "danger")

        return render_template("login.html")
    

    @app.route("/logout")
    @login_required
    def logout():
        """Wylogowanie użytkownika"""
        logout_user()
        return redirect(url_for("login"))


def register_expense_routes(app):
    """Trasy związane z wydatkami"""

    @app.route("/")
    @login_required
    def index():
        """Strona główna"""
        expenses = Expense.query.filter_by(user_id=current_user.id).all()
        category_totals = {}
        for expense in expenses:
            category = expense.category
            category_totals[category] = category_totals.get(category, 0) + float(
                expense.amount
            )

        return render_template(
            "index.html", expenses=expenses, category_totals=category_totals
        )

    @app.route("/add_expense", methods=["GET", "POST"])
    @login_required
    def add_expense():
        """Dodawanie nowego wydatku przez użytkownika"""
        if request.method == "POST":
            try:
                new_expense = handle_expense_form(request.form)
                db.session.add(new_expense)
                db.session.commit()
                flash("Wydatek dodany!", "success")
                return redirect(url_for("index"))

            except (KeyError, ValueError):
                flash("Wystąpił błąd w formularzu", "danger")

            except SQLAlchemyError as e:
                db.session.rollback()
                print(f"Błąd zapisu do bazy: {e}")
                flash("Wystąpił błąd podczas zapisu do bazy", "danger")

        return render_template("add_expense.html")

    @app.route("/edit_expense/<int:expense_id>", methods=["GET", "POST"])
    @login_required
    def edit_expense(expense_id):
        """Edycja istniejącego wydatku użytkownika"""
        expense = db.session.get(Expense, expense_id)
        if expense is None:
            abort(404)

        if expense.user_id != current_user.id:
            flash("Nie masz uprawnień", "danger")
            return redirect(url_for("index"))

        if request.method == "POST":
            expense.amount = request.form["amount"]
            expense.description = request.form["description"]
            expense.category = request.form["category"]
            expense.date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()

            db.session.commit()
            flash("Wydatek zaktualizowany", "success")
            return redirect(url_for("index"))

        return render_template("edit_expense.html", expense=expense)

    @app.route("/delete_expense/<int:expense_id>", methods=["POST"])
    @login_required
    def delete_expense(expense_id):
        """Usuwanie wybranego wydatku przez użytkownika"""
        expense = db.session.get(Expense, expense_id)
        if expense is None:
            abort(404)

        if expense.user_id != current_user.id:
            flash("Nie masz uprawnień", "danger")
            return redirect(url_for("index"))

        db.session.delete(expense)
        db.session.commit()
        flash("Wydatek usunięty", "success")
        return redirect(url_for("index"))
