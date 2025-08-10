"""Moduł inicjalizujący aplikację"""

from flask import Flask
from app.models import db
from app.routes import login_manager, init_routes
from config import Config


def create_app():
    """
    Tworzy i konfiguruje aplikację Flask.
    Inicjalizuje bazę danych, menadżera logowania i trasy.
    Tworzy tabele w bazie danych.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    init_routes(app)

    with app.app_context():
        db.create_all()

    return app
