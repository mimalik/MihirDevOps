from flask import Blueprint

dog_link = Blueprint('dog',__name__, url_prefix = '/dog')

@dog_link.route('/', methods = ['POST', 'GET'])
def greetDog():
    return "JELLO JOGGO"

@dog_link.route('/addDog/', methods = ['POST', 'GET'])
def addDog():
    return "Dog Added"

@dog_link.route('/showDog/', methods = ['POST', 'GET'])
    return "Name: %" % thisDog.name

@dog_link.route('/killDog/', methods = ['POST', 'GET'])
    return "Name: %" % thisDog.name
