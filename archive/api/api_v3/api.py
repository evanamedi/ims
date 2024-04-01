import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from api_v3.database import db


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print(f"database uri: {app.config['SQLALCHEMY_DATABASE_URI']}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

from api_v3 import api_routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)