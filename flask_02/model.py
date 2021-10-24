from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sql_interface import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    quantity = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.name

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True