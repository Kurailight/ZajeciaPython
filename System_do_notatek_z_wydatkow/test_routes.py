"""Testy jednostkowe i integracyjne"""

# pylint: disable=redefined-outer-name, missing-module-docstring
# pylint: disable=missing-function-docstring, contextmanager-generator-missing-cleanup

from unittest.mock import patch
from datetime import date
from uuid import uuid4
import pytest
from app import create_app, db
from app.models import User, Expense


@pytest.fixture
def client():
    """Fixture testowego klienta Flask z testową bazą danych"""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False

    with app.test_client() as client:  # symulacja żądan HTTP
        with app.app_context():
            db.create_all()
            # tworzenie unikalnego użytkownika
            unique_id = uuid4().hex
            user = User(username=f"user_{unique_id}", email=f"{unique_id}@test.com")
            user.set_password("testpass")
            db.session.add(user)
            db.session.commit()

            # logowanie ręcznie użytkownika -Flask-Login session
            with client.session_transaction() as sess:
                sess["_user_id"] = str(user.id)

        yield client

        with app.app_context():
            db.drop_all()


# taki sam test jak kolejny ale z mockiem
def test_add_expense_db_error(client):
    """
    Testuje, czy aplikacja poprawnie reaguje,
    gdy commit do bazy danych się nie powiedzie.
    """
    with patch("app.routes.db.session.commit") as mock_commit:
        mock_commit.side_effect = Exception("DB error")

        response = client.post(
            "/add_expense",
            data={
                "description": "Obiad",
                "amount": 25.5,
                "category": "Jedzenie",
                "date": date.today().isoformat(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200
        assert "Wystąpił błąd" in response.get_data(as_text=True)


def test_add_expense_success(client):
    """
    sprawdza, czy po poprawnym dodaniu wydatku przez endpoint /add_expense
    aplikacja zwraca kod 200 i zawiera w odpowiedzi opis dodanego wydatku
    """
    response = client.post(
        "/add_expense",
        data={
            "description": "Obiad",
            "amount": 25.5,
            "category": "Jedzenie",
            "date": date.today().isoformat(),
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Obiad" in response.data


def test_add_expense_missing_amount(client):
    """
    weryfikuje, czy po próbie dodania wydatku bez podania kwoty
    aplikacja zwraca stronę z kodem 200 i odpowiednim komunikatem o błędzie
    """
    response = client.post(
        "/add_expense",
        data={
            "description": "Obiad",
            "category": "Jedzenie",
            "date": date.today().isoformat(),
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert "Wystąpił błąd" in response.get_data(as_text=True)


def test_delete_expense(client):
    """
    dodaje wydatek do bazy, usuwa go przez endpoint /delete_expense/<id>,
    a następnie weryfikuje, że strona nie zawiera już usuniętego wydatku
    """
    with client.application.app_context():
        user = User.query.first()
        expense = Expense(
            description="Test",
            amount=10,
            category="Inne",
            date=date.today(),
            user_id=user.id,
        )
        db.session.add(expense)
        db.session.commit()
        expense_id = expense.id

    response = client.post(f"/delete_expense/{expense_id}", follow_redirects=True)
    assert response.status_code == 200
    assert b"Test" not in response.data


def test_display_expenses(client):
    """
    dodaje trzy wydatki do bazy, a następnie sprawdza,
    czy strona główna poprawnie je wyświetla
    """
    with client.application.app_context():
        user = User.query.first()
        db.session.add_all(
            [
                Expense(
                    description="A",
                    amount=10,
                    category="Jedzenie",
                    date=date.today(),
                    user_id=user.id,
                ),
                Expense(
                    description="B",
                    amount=20,
                    category="Transport",
                    date=date.today(),
                    user_id=user.id,
                ),
                Expense(
                    description="C",
                    amount=30,
                    category="Jedzenie",
                    date=date.today(),
                    user_id=user.id,
                ),
            ]
        )
        db.session.commit()

    response = client.get("/")
    assert response.status_code == 200
    assert b"A" in response.data
    assert b"B" in response.data
    assert b"C" in response.data


def test_frontend_filter_dropdown_exists(client):
    """
    sprawdza, czy strona główna zawiera dropdown do filtrowania wydatków według kategorii
    """
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert "Filtruj według kategorii" in html


def test_user_password_hashing():
    """
    weryfikuje, że funkcje ustawiania i sprawdzania hasła
    w modelu User działają prawidłowo: poprawne hasło przechodzi, a błędne jest odrzucane
    """
    user = User(username="testuser")
    user.set_password("password")

    # Sprawdzamy, czy hasło zostało ustawione poprawnie
    assert user.check_password("password") is True
    assert user.check_password("wrongpassword") is False


def test_expense_creation():
    """
    Testuje tworzenie obiektu Wydatek.
    Sprawdza, czy wszystkie pola są poprawnie ustawione przy inicjalizacji.
    """
    expense = Expense(
        description="Test Expense",
        amount=99.99,
        category="Test",
        date=date.today(),
        user_id=1,
    )

    assert expense.description == "Test Expense"
    assert expense.amount == 99.99
    assert expense.category == "Test"
    assert expense.date == date.today()
    assert expense.user_id == 1


def test_user_repr():
    """
    Testuje metodę __repr__ klasy User
    Sprawdza, czy reprezentacja tekstowa użytkownika zawiera jego username.
    """
    user = User(username="repruser")
    repr_str = repr(user)
    assert "repruser" in repr_str


def test_expense_repr():
    """
    Testuje metodę __repr__ klasy Expense
    Sprawdza, czy reprezentacja tekstowa wydatku zawiera jego opis i kwotę.
    """
    expense = Expense(
        description="Repr Test",
        amount=123.45,
        category="TestCat",
        date=date.today(),
        user_id=2,
    )
    repr_str = repr(expense)
    assert "Repr Test" in repr_str
    assert "123.45" in repr_str
