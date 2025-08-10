"""
Konfiguracja aplikacji flask.
Zawiera ustawienia klucza sekretnego, bazy danych oraz konfigurację ciasteczek sesji.
"""

import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Konfiguracja aplikacji"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "hvgce77fg3ry7uhu"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "baza.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(days=7)

