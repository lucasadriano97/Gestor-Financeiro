# filepath: LFA-Lucky-Financial-Assistant/LFA-Lucky-Financial-Assistant/src/main.py

from flask import Flask
from controllers import *
from services import *
from models import *
from utils import *

app = Flask(__name__)

# Configure routes
@app.route('/')
def home():
    return "Welcome to the Lucky Financial Assistant!"

if __name__ == '__main__':
    app.run(debug=True)