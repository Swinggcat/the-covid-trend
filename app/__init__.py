from flask import Flask

app = Flask(__name__)

# Load Controllers
from .controller import *
