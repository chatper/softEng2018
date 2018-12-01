import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv('.flaskenv')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ[
    "SQLALCHEMY_TRACK_MODIFICATIONS"]

db = SQLAlchemy(app)

# Register routes
import controllers.api.users


# Register custom commands
@app.cli.command()
def init_db():
    import scripts.initialize_db


if __name__ == "__main__":
    app.run()
