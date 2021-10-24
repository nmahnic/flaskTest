python3 -m venv flask_04

source flask_04/bin/activate

deactivate

pip3 install -r requirements.txt


https://rahmanfadhil.com/flask-rest-api/




POST:
```
curl -d '{"user":"tiago", "meter_id":null}' -H "Content-Type: application/json" -X POST http://localhost:4000/users

curl -d '{"user":"tiago", "meter_id":1}' -H "Content-Type: application/json" -X POST http://localhost:4000/usersmeter
```