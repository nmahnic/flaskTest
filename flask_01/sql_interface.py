from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/mash/Documents/flask_01/test_01.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    pais = db.Column(db.String)

    def __repr__(self):
        return "<Equipo %r>" % self.nombre

if __name__ == "__main__":
    app.run(debug=True)