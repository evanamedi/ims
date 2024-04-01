import os
from dotenv import load_dotenv
import mysql.connector

# load environment variables from .env file
load_dotenv()

def create_connection():
    cnx = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    
    return cnx