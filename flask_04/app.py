from flask import Flask, jsonify, request
from sql_interface import app
from model import User, UserSchema, Meter, MeterSchema, db

@app.route('/ping')
def ping():
    return 'Pong!'

@app.route('/')
def root():
    return jsonify({"message": "Pong!"})

@app.route('/meters', methods=['GET'])
def getMeter():
    try:
        allUser = Meter.query.all()
    except:
        allUser = []
    userSchema = MeterSchema(many=True)
    return jsonify(userSchema.dump(allUser))

@app.route('/users', methods=['GET', 'POST'])
def getUsers():
    userSchema = UserSchema(many=True)
    if request.method == 'POST':
        data = request.json
        print(data)

        try:
            selectedUser = User.query.filter(User.name == data['user']).first()
            print(selectedUser)
        except:
            response = {'message': 'error1'}
            return jsonify(response)
        if(selectedUser == None):
            try:
                newUser = User(name=data['user'], meter_id = data['meter_id'])
                db.session.add(newUser)
                db.session.commit()
                response = {'message': 'success'}
                return jsonify(response)
            except:
                response = {'message': 'error2'}
                return jsonify(response)
        else:
            print(selectedUser.name)
            response = {'message': 'wrong'}
            return jsonify(response)

    else:
        try:
            allUser = User.query.all()
        except:
            allUser = []
        return jsonify(userSchema.dump(allUser))

@app.route('/usersmeter', methods=['POST'])
def joinUser():
    userSchema = UserSchema(many=True)
    data = request.json
    print(data)

    try:
        selectedUser = db.session.query(User.name, Meter.mac).join(Meter).all()
        print(selectedUser)
        return jsonify(userSchema.dump(selectedUser))
    except:
        response = {'message': 'error1'}
        return jsonify(response)
    


if __name__ == "__main__":
    app.run(debug=True, port=4000)