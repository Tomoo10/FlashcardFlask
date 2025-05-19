from flask import Flask, render_template, url_for, redirect, request, session, flash
from pathlib import Path
from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate
import os

#flask + database
app = Flask(__name__)
migrate = Migrate()

database_url = os.environ["DATABASE_URL"]
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.instance_path = Path("./data").resolve()
#manage user login+logout
app.secret_key = 'supersecretkey'

db.init_app(app)
migrate.init_app(app, db)

from user import user_bp
from index import index_bp
from set import set_bp
from quiz import quiz_bp
app.register_blueprint(user_bp)
app.register_blueprint(index_bp)
app.register_blueprint(set_bp)
app.register_blueprint(quiz_bp)


if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=True)