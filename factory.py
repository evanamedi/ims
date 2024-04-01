from flask import Flask
from api_v3.database import db
import os
from dotenv import load_dotenv
from api_v3.api_routes import api_bp
from flask_cors import CORS

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    db.init_app(app)
    app.register_blueprint(api_bp, url_prefix='/api')
    CORS(app)
    # CORS(app, origins=["http://localhost:5000", "http://example.com"]) this is for production environment
    return app