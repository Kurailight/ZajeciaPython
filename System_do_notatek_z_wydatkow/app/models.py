"""Moduł definiujący modele bazy danych: Użytkownika i wydatek"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """Model reprezentujący użytkownika aplikacji"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    expenses = db.relationship("Expense", backref="owner", lazy=True)

    def set_password(self, password):
        """Haszuje i ustawia hasło użytkownika"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Sprawdza, czy podane hasło jest poprawne"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Zwraca reprezentację tekstową użytkownika"""
        return f"<User username={self.username}>"


class Expense(db.Model):
    """Model reprezentujący wydatek"""

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    category = db.Column(db.String(100))
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """Zwraca reprezentację tekstową wydatku"""
        return f"<Expense description={self.description} amount={self.amount}>"
