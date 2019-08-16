from flask import Flask, request
from flask_mongoengine import MongoEngine
from mongoengine import *

app = Flask(__name__)
app.config['MONGODB_DB'] = 'admin'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'dad'
app.config['MONGODB_PASSWORD'] = 'root'

db = MongoEngine(app)

class Dogs(db.Document):
    __collection__ = 'dogs'
    name = StringField()
    age = IntField()

    def __repr__(self):
        return '<DOGGY> %' % self.name

@app.route('/', methods = ['POST', 'GET'])
def wow():
    return "Hello Beess"

@app.route('/addDog/', methods = ['POST', 'GET'])
def addDog():
    dAge = request.values.get("dAge", type = int, default = 0)
    dName = request.values.get("dName", type = str, default = None)
    newDog = Dogs(name = dName, age = dAge)
    newDog.save()
    return "Dog Added"

@app.route('/modDog/', methods = ['POST', 'GET'])
def modDog():
    dName = request.values.get("dName", type=str, default=None)
    modName = request.values.get("newName", type=str, default = None)
    newDog = Dogs.objects(name = dName).modify(set__name = modName, new = True)
    return newDog.name

@app.route('/killDog/', methods = ['POST', 'GET'])
def killDog():
    dName = request.values.get("dName", type=str, default=None)
    newDog = Dogs.objects(name = dName)
    killed = newDog.delete()
    return str(killed)

@app.route('/findDog/', methods = ['POST', 'GET'])
def findDog():
    dName = request.values.get("dName", type=str, default=None)
    firstDog = Dogs.objects(name = dName).first()
    if firstDog == None:
        return "Lost Dog"
    return str(firstDog.age)

@app.route('/fullKennel/', methods = ['POST', 'GET'])
def kennel():
    return

if __name__ == '__main__':
   app.run(debug = True)
