__author__ = 'joe'
from flask import Blueprint

home = Blueprint('home', __name__)

from .import views