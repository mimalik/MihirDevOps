from flask import Flask, render_template, request, make_response
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename

app = Flask(__name__)

# Connect SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/myDBtest'
app.config['SECRET_KEY'] = 'ABCD'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myDBtest'

mysql = MySQL(app)
db = SQLAlchemy(app)

# Testable class to store a test table.
class testable(db.Model):
    id = db.Column('ID', db.Integer, primary_key = True)#, autoincrement = True)
    firstName = db.Column('firstName', db.String(10))
    lastName = db.Column('lastName', db.String(10))

    def __init__(self, id, fname, lname):
        self.id = id
        self.firstName = fname
        self.lastName = lname

    def __repr__(self):
        return '<Name %>' % self.firstName
# shytable class to check relations between tables and test out foriegn keys
# class shytable(db.Model):
#     id = db.Column('ShyID', ForeignKey(testable.id), primary_key = True, autoincrement = True)
#     def __init__(self,id):
#         self.id = id
#     def __repr__(self):
#         return 'ID %' %self.id

# test object of testable class

Mihir = testable(1, 'Mihir', 'Malik')
@app.route('/mySQLcreate', methods = ['GET', 'POST'])
def creatMySql():
    if request.method == 'POST':
        id = '123'
        firstName = 'Mihir'
        lastName = 'Malik'
        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO MyUsers(id, firstName, lastName) VALUES (%d, %s, %s)", (id, firstName, lastName))
        mysql.connection.commit()
        curs.close()
        return 'Successfully created'
    return 'or Not created'


@app.route('/createDB/', methods = ['POST'])
def createDB():
    if request.method == 'POST':
        db.session.add(Mihir)
        db.session.commit()
        db.create_all()
        return 'Created Table'
    return 'Not created'

@app.route('/addID/<id>', methods = ['POST'])
def addID(id):
    if request.method == 'POST':
        num = 3
        firstName = id
        lastName = id

        newID = testable(num, id, id)
        db.session.add(newID)
        db.session.commit()
        return 'Added successfully'
    return 'Failure'

if __name__ == '__main__':
   app.run(debug = True)
