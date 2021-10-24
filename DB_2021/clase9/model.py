import sqlobject as so
import os

# os.getcwd() -> '/home/mash/Documents/DB_2021/clase9'
# connection = so.connectionForURI("sqlite://"+os.getcwd()+"/albums.sqlite")
connection = so.connectionForURI("sqlite://"+os.getcwd()+"/test_04.sqlite3")
so.sqlhub.processConnection = connection

"""class Artist(so.SQLObject):
    name = so.StringCol(length=120, varchar=True)

class Album(so.SQLObject):
    title = so.StringCol(length=160, varchar=True)
    artist = so.ForeignKey('Artist', default=None)

def to_dict(obj):
    d = dict((c,getattr(obj,c)) for c in obj.sqlmeta.columns)
    d['id'] = obj.id
    return d

def finder(name):
    artist = Artist.selectBy(name=name).getOne()
    albums = Album.select(Album.q.artist == artist)
    d = to_dict(artist)
    d['albums'] = [to_dict(album) for album in albums]
    return d"""

class User(so.SQLObject):
    name = so.StringCol(length=120, varchar=True)

class Meter(so.SQLObject):
    mac = so.StringCol(length=160, varchar=True)
    #user_id = so.ForeignKey('User', default=None)

def to_dict(obj):
    d = dict((c,getattr(obj,c)) for c in obj.sqlmeta.columns)
    d['id'] = obj.id
    return d

def finder(name):
    id = User.selectBy(name=name).getOne()
    albums = User.select(User.q.user_id == id)
    d = to_dict(id)
    d['albums'] = [to_dict(album) for album in albums]
    return d

def printUser(name):
    return User.selectBy(name=name).getOne()

def printMeter(id):
    meter = Meter.selectBy(id=id).getOne()
    return meter.mac

def printModel(name):
    user = printUser(name)
    print("USER_METER ->",user.name,printMeter(user.id))