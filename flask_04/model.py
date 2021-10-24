from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
from flask_marshmallow import Marshmallow
from sql_interface import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    meter_id = db.Column(db.Integer, db.ForeignKey("Meter.id"), nullable=True)
    
    # OJO!
    meter = db.relationship("Meter", backref='parents')
    
    def __repr__(self):
        return "<User %r>" % self.name


class Meter(db.Model):
    __tablename__ = "Meter"

    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String, unique=True)


    def __repr__(self):
        return "<Meter %r>" % self.name



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class MeterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meter
        load_instance = True