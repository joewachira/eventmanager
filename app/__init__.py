__author__ = 'joe'

from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
	app = Flask(__name__, template_folder="Designs")

	Bootstrap(app)

	# register blueprints

	return app