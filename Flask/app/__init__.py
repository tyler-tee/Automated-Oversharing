import os
from flask import Flask
from sqlmodel import SQLModel, create_engine
from .blog import blog_pages


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("flask_secret_key")
    app.engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(app.engine)

    # Register blueprints
    app.register_blueprint(blog_pages)

    return app
