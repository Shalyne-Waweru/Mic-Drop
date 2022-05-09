from flask import render_template,redirect,url_for
from app import app
from .models import pickup_lines,interview
from .forms import PickupLineForm, InterviewForm

Pickup = pickup_lines.Pickup
Interview = interview.Interview

# LANDING PAGE
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# PICKUP LINES PAGE
@app.route('/pickup-lines', methods = ['GET','POST'])
def pickup():
    '''
    View root page function that returns the pickup lines page and its data
    '''

    #Create an instance of the PickupLineForm class and name it pickup_line_form
    pickup_line_form = PickupLineForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if pickup_line_form.validate_on_submit():
        #If True we gather the data from the form input fields
        pickupLine = pickup_line_form.pickupLine.data

        #Create a new pickup_line object and save it
        new_pickup_line = Pickup(pickupLine)
        new_pickup_line.save_pickup_line()

        return redirect(url_for('pickup'))

    #Get all the Pickup Lines
    pickup_lines = Pickup.get_pickup_lines()

    return render_template('pickup-lines.html', pickup_line_form = pickup_line_form, pickup_lines = pickup_lines)

# INTERVIEW PITCHES PAGE
@app.route('/interview', methods = ['GET','POST'])
def interview():
    '''
    View root page function that returns the interview pitches page and its data
    '''

    #Create an instance of the InterviewForm class and name it interview_form
    interview_form = InterviewForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if interview_form.validate_on_submit():
        #If True we gather the data from the form input fields
        interview = interview_form.interview.data

        #Create a new interview object and save it
        new_interview = Interview(interview)
        new_interview.save_interview()

        return redirect(url_for('interview'))

    #Get all the Interview Pitches
    interview_pitches = Interview.get_interviews()

    return render_template('interview-pitches.html', interview_form = interview_form, interview_pitches = interview_pitches)