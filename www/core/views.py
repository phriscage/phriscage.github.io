""" core view Blueprint for root level paths """
from flask import Blueprint, render_template

core = Blueprint('core', __name__, template_folder='../../')

@core.route('/', methods=['GET'])
def get_index():
    """ root path for index """
    return render_template('index.html')
