import MySQLdb as m
m

dir(m)

conn = m.connect(host='localhost', user='guest', password='guest', db='Chinook')

conn

cur = conn.cursor()

cur

cur.execute("SELECT * FROM Artist")

cur.rowcount

cur.fetchone()
# (3, 'Aerosmith')

for artist in cur.fetchmany(10):
	print(artist)

cur.execute("SELECT Name FROM Artist")
artist = [artist[0] for artist in cur.fetchall()]

for art in artist:
	print(art)

artist.sort()

for art in artist:
	print(art)


cur.execute("SELECT Name FROM Artist")
#275
artist = [artist[0] for artist in cur.fetchall()]
artist[:5]
#['AC/DC', 'Accept', 'Aerosmith', 'Alanis Morissette', 'Alice In Chains']

cur.close() #cursor tupla de tuplas
conn.close()





conn = m.connect(host='localhost', user='guest', password='guest', db='Chinook')
cur = conn.cursor(cursorclass=m.cursors.DictCursor)
cur
#<MySQLdb.cursors.DictCursor object at 0x7f615a146190>

cur.execute("SELECT * FROM Artist")
#275
a = cur.fetchone()
#{'ArtistId': 1, 'Name': 'AC/DC'}
a.keys()
dict_keys(['ArtistId', 'Name'])

#todo lo mismo
for k in a.keys():
	print(k, a[k])

for k in a:
	print(k, a[k])

for k in list(a.keys()):
	print(k, a[k])


for artist in cur.fetchmany(5):
	print(artist['Name']


artist = [a['Name'] for a in cur.fetchall()]

cur.close()
conn.close()

