from flask import Flask, jsonify
from products import products
from sql_interface import app
from model import Product, ProductSchema


#app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong!'

@app.route('/')
def root():
    return jsonify({"message": "Pong!"})

@app.route('/products/', methods=['GET'])
def getProducts():
    try:
        prod = Product.query.all()
    except:
        prod = []
    prod_schema = ProductSchema(many=True)
    return jsonify(prod_schema.dump(prod))

@app.route('/products/file', methods=['GET'])
def getProductsFile():
    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True, port=4000)