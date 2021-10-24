import sqlobject as so
import os
import defs

connection = so.connectionForURI('mysql://{}:{}@{}/{}'.format(defs.USER,defs.PASSWORD,defs.HOST,defs.DBASE))
so.sqlhub.processConnection = connection


class User(so.SQLObject):
    class sqlmeta:
        table = "User"
    # userID = so.IntCol()
    name = so.StringCol(length=50, varchar=True)
    surname = so.StringCol(length=50, varchar=True)
    userName = so.StringCol(length=50, varchar=True)
    passwd = so.StringCol(length=50, varchar=True)
    mail = so.StringCol(length=80, varchar=True)


class Meter(so.SQLObject):
    class sqlmeta:
        table = "Meter"
    # meterId = so.IntCol()
    mac = so.StringCol(length=50, varchar=True)
    ip = so.StringCol(length=50, varchar=True)
    userId = so.ForeignKey('User', default=None)
    dumId = so.ForeignKey('DUM', default=None)

class DUM(so.SQLObject):
    class sqlmeta:
        table = "DUM"
    # dumId = so.IntCol()
    userId = so.ForeignKey('User', default=None)
    name = so.StringCol(length=50, varchar=True)
    dumId = so.ForeignKey('DUM', default=None)

class Measure(so.SQLObject):
    class sqlmeta:
        table = "Measure"
    # measureId = so.IntCol(),
    dumId = so.ForeignKey('DUM', default=None),
    timestamp = so.TimestampCol(),
    vrms = so.FloatCol(),
    irms = so.FloatCol(),
    activePower = so.FloatCol(),
    pf = so.FloatCol(),
    thd = so.FloatCol(),
    cosPhi = so.FloatCol(),
    freq_1st = so.FloatCol(),
    freq_2nd = so.FloatCol(),
    freq_3rd = so.FloatCol(),
    freq_4th = so.FloatCol(),
    freq_5th = so.FloatCol(),
    freq_6th = so.FloatCol(),
    freq_7th = so.FloatCol(),
    freq_8th = so.FloatCol(),
    freq_9th = so.FloatCol(),
    freq_10th = so.FloatCol()


"""def to_dict(obj):
    d = dict((c, getattr(obj, c)) for c in obj.sqlmeta.columns)
    d['UserID'] = obj.userId
    return d


def finder(name):
    user = User.selectBy(name=name).getOne()
    meters = Meter.select(Meter.userId == user.userId)
    d = to_dict(user)
    d['meter'] = [to_dict(meter) for meter in meters]
    return d"""

"""def printUser(name):
    return User.selectBy(User.name==name).getOne()"""

def printModel():
    print( User.select())