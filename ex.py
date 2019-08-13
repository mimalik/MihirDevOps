from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import *

app = Flask(__name__)
app.config['MONGODB_DB'] = 'test'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'root'
app.config['MONGODB_PASSWORD'] = 'root'

db = MongoEngine(app)
class Dogs(Document):
    __collection__ = 'dogs'
    id = IntField()
    name = StringField()
    age = IntField()
    meta = {
        'db_alias': 'root',
        'collection': 'dogs'
    }
    def __repr__(self):
        return '<DOGGY> %' % self.name

    # def __init__(self, id, name, age):
    #     self.id = id
    #     self.name = name
    #     self.age = age
    #     return "wuf"

@app.route('/createMongoDB/', methods = ['POST', 'GET'])
def createMongoDB():
    db.register_connection(alias = 'root', name = 'test')
    db.register([Dogs])
    newDog = Dogs(id = 0, name = "Zero", age = 0)
    newDog.save()

@app.route('/findDog', methods = ['POST', 'GET'])
def findDog():
    dId = request.values.get("dogID", type=int, default=None)
    firstDog = db.Dogs.objects.first_or_404(id = dId)
if __name__ == '__main__':
   app.run(debug = True)
