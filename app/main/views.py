from flask import render_template,redirect,url_for
from . import main
from ..models import Pickup,Interview,Promotion,Comments
from .forms import PickupLineForm, InterviewForm, PromotionForm, CommentForm

# LANDING PAGE
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# PICKUP LINES PAGE
@main.route('/pickup-lines', methods = ['GET','POST'])
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

        return redirect(url_for('main.pickup'))

    #Get all the Pickup Lines
    pickup_lines = Pickup.get_pickup_lines()

    return render_template('pickup-lines.html', pickup_line_form = pickup_line_form, pickup_lines = pickup_lines)

# INTERVIEW PITCHES PAGE
@main.route('/interview', methods = ['GET','POST'])
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

        return redirect(url_for('main.interview'))

    #Get all the Interview Pitches
    interview_pitches = Interview.get_interviews()

    return render_template('interview-pitches.html', interview_form = interview_form, interview_pitches = interview_pitches)

# PROMOTION PITCHES PAGE
@main.route('/promotion', methods = ['GET','POST'])
def promotion():
    '''
    View root page function that returns the promotion pitches page and its data
    '''

    #Create an instance of the PromotionForm class and name it promotion_form
    promotion_form = PromotionForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if promotion_form.validate_on_submit():
        #If True we gather the data from the form input fields
        promotion = promotion_form.promotion.data

        #Create a new promotion object and save it
        new_promotion = Promotion(promotion)
        new_promotion.save_promotion()

        return redirect(url_for('main.promotion'))

    #Get all the Promotion Pitches
    promotion_pitches = Promotion.get_promotions()

    return render_template('promotion-pitches.html', promotion_form = promotion_form, promotion_pitches = promotion_pitches)

# COMMENTS PAGE
@main.route('/comments', methods = ['GET','POST'])
def comments():

    #Create an instance of the CommentForm class and name it comments_form
    comments_form = CommentForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if comments_form.validate_on_submit():
        #If True we gather the data from the form input fields
        comment = comments_form.comment.data

        #Create a new comment object and save it
        new_comment = Comments(comment)
        new_comment.save_comment()

        return redirect(url_for('main.comments'))

    #Get all the Comments
    all_comments = Comments.get_comments()

    return render_template('comments.html', comments_form = comments_form, all_comments = all_comments)