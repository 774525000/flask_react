from flask import Flask
from flask_restful import Api, Resource 
from flask_cors import CORS


app = Flask(__name__, template_folder = './build', static_folder='./build/static')
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


from app import routes
from app import apis