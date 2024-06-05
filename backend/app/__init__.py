from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mongo = PyMongo(app)
CORS(app)

from app import routes, models

@app.cli.command("migrate-db")
def migrate_db():
    """Perform database migrations."""
    from app.models import User
    
    with app.app_context():
        db.create_all()
        print("Database migrations completed.")

if __name__ == "__main__":
    app.run()
