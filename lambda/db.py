import psycopg2
import os
from dotenv import load_dotenv

# reads .env file and loads all variables
load_dotenv()  

# create and returns a connection to the Postgres database
def get_connection():
    return psycopg2.connect(
        host = os.environ['DB_HOST'],
        database = os.environ['DB_NAME'],
        user = os.environ['DB_USER'],
        password = os.environ['DB_PASSWORD'],
        port = os.environ['DB_PORT']
    )
