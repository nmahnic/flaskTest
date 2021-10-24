from sql_interface import db

db.create_all()


from sql_interface import Equipo


barcelona = Equipo(nombre="Barca", pais="Esp")
athletic = Equipo(nombre="Athletic", pais="Esp")
boca = Equipo(nombre="Boke", pais="Arg")
river = Equipo(nombre="River", pais="Arg")
chaca = Equipo(nombre="Chaca", pais="Arg")

db.session.add(barcelona)
db.session.add(athletic)
db.session.add(boca)
db.session.add(river)
db.session.add(chaca)

db.session.commit()

athletic.nombre = "Atleti"

db.session.commit()

result = Equipo.query.all()
for r in result:
    print(r.nombre)

print()
bar = Equipo.query.filter_by(nombre="Barca").first()
print(bar.nombre)

print()
chel = Equipo.query.filter_by(nombre="Atleti").all()
for r in chel:
    print(r.nombre)

print()
riv = Equipo.query.filter(Equipo.nombre=="River").first()
print(riv.nombre)

db.session.delete(riv)
db.session.commit()