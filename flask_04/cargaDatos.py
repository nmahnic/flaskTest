from model import User, Meter, db

db.create_all()

mash =   User(name="Mash", meter_id=1)
juanma = User(name="Juanma", meter_id=2)
eric =   User(name="Eric", meter_id=3)

"""mash =   User(name="Mash")
juanma = User(name="Juanma")
eric =   User(name="Eric")"""

mashMeter =   Meter(mac="8C-10-D4-88-7C-A4")
juanmaMeter = Meter(mac="84-D8-1B-0C-5B-C1")
ericMeter =   Meter(mac="B0-B2-8F-1D-4D-02")

db.session.add(mash)
db.session.add(juanma)
db.session.add(eric)

db.session.commit()

db.session.add(mashMeter)
db.session.add(juanmaMeter)
db.session.add(ericMeter)

db.session.commit()

result = User.query.all()
for r in result:
    print(r.name)

result = Meter.query.all()
for r in result:
    print(r.mac)
