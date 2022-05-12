from flask import render_template,redirect,url_for
import flask_login
from . import main
from ..models import Pickup,Interview,Promotion,PickupComments,PickupLikes,PickupDislikes
from .forms import PickupLineForm, InterviewForm, PromotionForm, CommentForm
from flask_login import current_user, login_required

# LANDING PAGE
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# PICKUP LINES PAGE
@main.route('/pickup-lines', methods = ['GET','POST'])
@login_required
def pickup():
    '''
    View root page function that returns the pickup lines page and its data
    '''

    #Create an instance of the PickupLineForm class and name it pickup_line_form
    pickup_line_form = PickupLineForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if pickup_line_form.validate_on_submit():
        # If True we gather the data from the form input fields
        pickupLine = pickup_line_form.pickupLine.data

        #Create a new pickup_line object and save it
        new_pickup_line = Pickup(pickupLine = pickupLine)
        new_pickup_line.save_pickup_line()
        flask_login.current_user.addPickupLine(new_pickup_line)

        return redirect(url_for('main.pickup'))

    #Get all the Pickup Lines
    pickup_lines = Pickup.get_pickup_lines()

    return render_template('pickup-lines.html', pickup_line_form = pickup_line_form, pickup_lines = pickup_lines)

#PICKUP COMMENTS PAGE
@main.route('/comments/<int:pickup_id>', methods = ['GET','POST'])
@login_required
def comments(pickup_id):
    '''
    View root page function that returns the pickup comments page and its data
    '''

    pline = Pickup.query.filter_by(id = pickup_id).first().pickupLine
    print(pline)
    pline_author = Pickup.query.filter_by(id = pickup_id).first().user.username
    print(pline_author)
    pline_postedDate = Pickup.query.filter_by(id = pickup_id).first().postedDate
    print(pline_postedDate)
    pline_likes = PickupLikes.query.filter_by(pickup_id = pickup_id).count()
    print(pline_likes)
    pline_dislikes = PickupDislikes.query.filter_by(pickup_id = pickup_id).count()
    print(pline_dislikes)

    #Create an instance of the CommentForm class and name it comments_form
    comments_form = CommentForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if comments_form.validate_on_submit():
        #If True we gather the data from the form input fields
        comment = comments_form.comment.data

        #Create a new comment object and save it
        new_comment = PickupComments(comment=comment, user=current_user, pickup_id=pickup_id )
        new_comment.save_comment()

        return redirect(url_for('main.comments',pickup_id=pickup_id))

    #Get all the Comments
    all_comments = PickupComments.get_comments(pickup_id)

    return render_template('pickup-comments.html', comments_form = comments_form, all_comments = all_comments, pickup_id = pickup_id, pline = pline, pline_author = pline_author, pline_postedDate = pline_postedDate, pline_likes = pline_likes, pline_dislikes = pline_dislikes)


#PICKUP LINE UPVOTES
@main.route('/like/<int:id>', methods = ['GET', 'POST'])
def pline_upvotes(id):
    pline_upvotes = PickupLikes.get_pickuplikes(id)

    valid_string = f'{current_user.id}:{id}'

    for pline in pline_upvotes:
        to_str = f'{pline}'

        print(valid_string+" "+to_str)

        if valid_string == to_str:
            return redirect(url_for('main.pickup',id=id))
        else:
            continue

    new_pline_upvote = PickupLikes(user = current_user, pickup_id=id)
    new_pline_upvote.save_pickuplike()

    return redirect(url_for('main.pickup',id=id))

#PICKUP LINE DOWNVOTES
@main.route('/dislike/<int:id>', methods = ['GET', 'POST'])
def pline_downvotes(id):
    pline_downvotes = PickupDislikes.get_pickupdislikes(id)

    valid_string = f'{current_user.id}:{id}'

    for pline in pline_downvotes:
        to_str = f'{pline}'

        print(valid_string+" "+to_str)

        if valid_string == to_str:
            return redirect(url_for('main.pickup',id=id))
        else:
            continue

    new_pline_downvote = PickupDislikes(user = current_user, pickup_id=id)
    new_pline_downvote.save_pickupdislike()

    return redirect(url_for('main.pickup',id=id))

# INTERVIEW PITCHES PAGE
@main.route('/interview', methods = ['GET','POST'])
@login_required
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
        new_interview = Interview(interview = interview)
        new_interview.save_interview()
        flask_login.current_user.addInterview(new_interview)

        return redirect(url_for('main.interview'))

    #Get all the Interview Pitches
    interview_pitches = Interview.get_interviews()

    return render_template('interview-pitches.html', interview_form = interview_form, interview_pitches = interview_pitches)

# PROMOTION PITCHES PAGE
@main.route('/promotion', methods = ['GET','POST'])
@login_required
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
        new_promotion = Promotion(promotion = promotion)
        new_promotion.save_promotion()
        flask_login.current_user.addPromotion(new_promotion)

        return redirect(url_for('main.promotion'))

    #Get all the Promotion Pitches
    promotion_pitches = Promotion.get_promotions()

    return render_template('promotion-pitches.html', promotion_form = promotion_form, promotion_pitches = promotion_pitches)
