from model import Product, db

db.create_all()

laptop = Product(name="Laptop", price=400, quantity=3)
mouse = Product(name="Mouse", price=40, quantity=2)
monitor = Product(name="Monitor", price=100, quantity=5)

db.session.add(laptop)
db.session.add(mouse)
db.session.add(monitor)

db.session.commit()

result = Product.query.all()
for r in result:
    print(r.name)
