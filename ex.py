from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import *

app = Flask(__name__)
app.config['MONGODB_DB'] = 'client_db'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'admin'
app.config['MONGODB_PASSWORD'] = 'admin@123'

db = MongoEngine(app)
class Dogs(db.Document):
    __collection__ = 'dogs'
    name = StringField()
    age = IntField()
    def __repr__(self):
        return '<DOGGY> %' % self.name

    # def __init__(self, id, name, age):
    #     self.id = id
    #     self.name = name
    #     self.age = age
    #     return "wuf"

@app.route('/createMongoDB/', methods = ['POST', 'GET'])
def createMongoDB():
    newDog = Dogs(name = "Zero", age = 0)
    newDog.save()
    return "True"

@app.route('/findDog', methods = ['POST', 'GET'])
def findDog():
    dId = request.values.get("dogID", type=int, default=None)
    firstDog = db.Dogs.objects.first_or_404(id = dId)
if __name__ == '__main__':
   app.run(debug = True)
