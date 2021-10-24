from leerDatos import DbInterfaces
from flask import jsonify
from products import products

result = DbInterfaces.read()
print(result)
#print(jsonify({result}))

print(products)
#print(jsonify(products))

