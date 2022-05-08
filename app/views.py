from flask import render_template
from app import app
from .forms import PickupLineForm

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/pickup-lines')
def pickup():

    pickup_line_form = PickupLineForm()

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('pickup-lines.html', pickup_line_form = pickup_line_form)