from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from authors_app.controllers.auth_controllers import auth

from authors_app.extensions import db, migrate

from authors_app.extensions import bcrypt

from authors_app.extensions import bcrypt



# db = SQLAlchemy()
# migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize SQLAlchemy and Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import models
    from authors_app.models.user import User
    from authors_app.models.books import Book
    from authors_app.models.company import company

    @app.route('/')
    def home():
        return "Hello programmers"
    
    app.register_blueprint(auth)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

