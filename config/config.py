# config file 
from dotenv import load_dotenv

load_dotenv()
import os

DATABASE_URI = os.getenv('DATABASE_URI')
