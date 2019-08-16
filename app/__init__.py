from flask import Flask

app = Flask(__name__, static_folder = "app")

app.config.from_json('config.json')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

db = MongoEngine(app)

@app.route("/")
def basePage():
    return "Don't Fear the silence, try to fill it"

from app.module.dog.controllers import dog_link as dog_module

app.register_blueprint(dog_module)
