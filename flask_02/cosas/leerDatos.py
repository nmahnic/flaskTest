from sql_interface import Product


class DbInterfaces:
    
    def read():
        result = Product.query.all()
        res = []
        for r in result:
            res.append(dict(name = r.name, price = r.price, quantity = r.quantity))
        return res