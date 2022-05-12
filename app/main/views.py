from flask import render_template,redirect,url_for
import flask_login
from . import main
from ..models import Pickup,PickupComments,PickupLikes,PickupDislikes,Interview,InterviewComments,InterviewLikes,InterviewDislikes,Promotion,PromotionComments,PromotionLikes,PromotionDislikes
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
        new_pickup_line = Pickup(pickupLine = pickupLine, user=current_user)
        new_pickup_line.save_pickup_line()

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
        new_interview = Interview(interview = interview, user=current_user)
        new_interview.save_interview()

        return redirect(url_for('main.interview'))

    #Get all the Interview Pitches
    interview_pitches = Interview.get_interviews()

    return render_template('interview-pitches.html', interview_form = interview_form, interview_pitches = interview_pitches)

#INTERVIEW PITCHES COMMENTS PAGE
@main.route('/interviewcomments/<int:interview_pitch_id>', methods = ['GET','POST'])
@login_required
def interviewComments(interview_pitch_id):
    '''
    View root page function that returns the interview pitch comments page and its data
    '''

    interview_pitch = Interview.query.filter_by(id = interview_pitch_id).first().interview
    print(interview_pitch)
    interview_author = Interview.query.filter_by(id = interview_pitch_id).first().user.username
    print(interview_author)
    interview_postedDate = Interview.query.filter_by(id = interview_pitch_id).first().postedDate
    print(interview_postedDate)
    interview_likes = InterviewLikes.query.filter_by(interview_pitch_id = interview_pitch_id).count()
    print(interview_likes)
    interview_dislikes = InterviewDislikes.query.filter_by(interview_pitch_id = interview_pitch_id).count()
    print(interview_dislikes)

    #Create an instance of the CommentForm class and name it comments_form
    comments_form = CommentForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if comments_form.validate_on_submit():
        #If True we gather the data from the form input fields
        comment = comments_form.comment.data

        #Create a new comment object and save it
        new_comment = InterviewComments(comment=comment, user=current_user, interview_pitch_id=interview_pitch_id )
        new_comment.save_interviewComment()

        return redirect(url_for('main.interviewComments',interview_pitch_id=interview_pitch_id))

    #Get all the Comments
    all_comments = InterviewComments.get_interviewComments(interview_pitch_id)

    return render_template('interview-comments.html', comments_form = comments_form, all_comments = all_comments, interview_pitch_id = interview_pitch_id, interview_pitch = interview_pitch, interview_author = interview_author, interview_postedDate = interview_postedDate, interview_likes = interview_likes, interview_dislikes = interview_dislikes)

#INTERVIEW PITCHES UPVOTES
@main.route('/interviewlike/<int:id>', methods = ['GET', 'POST'])
def interview_upvotes(id):
    interview_upvotes = InterviewLikes.get_interviewlikes(id)

    valid_string = f'{current_user.id}:{id}'

    for interview in interview_upvotes:
        to_str = f'{interview}'

        print(valid_string+" "+to_str)

        if valid_string == to_str:
            return redirect(url_for('main.interview',id=id))
        else:
            continue

    new_interview_upvote = InterviewLikes(user = current_user, interview_pitch_id=id)
    new_interview_upvote.save_interviewlike()

    return redirect(url_for('main.interview',id=id))

#INTERVIEW PITCHES DOWNVOTES
@main.route('/interviewdislike/<int:id>', methods = ['GET', 'POST'])
def interview_downvotes(id):
    interview_downvotes = InterviewDislikes.get_interviewdislikes(id)

    valid_string = f'{current_user.id}:{id}'

    for interview in interview_downvotes:
        to_str = f'{interview}'

        print(valid_string+" "+to_str)

        if valid_string == to_str:
            return redirect(url_for('main.interview',id=id))
        else:
            continue

    new_interview_downvote = InterviewDislikes(user = current_user, interview_pitch_id=id)
    new_interview_downvote.save_interviewdislike()

    return redirect(url_for('main.interview',id=id))

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
        new_promotion = Promotion(promotion = promotion, user=current_user)
        new_promotion.save_promotion()

        return redirect(url_for('main.promotion'))

    #Get all the Promotion Pitches
    promotion_pitches = Promotion.get_promotions()

    return render_template('promotion-pitches.html', promotion_form = promotion_form, promotion_pitches = promotion_pitches)

#PROMOTION PITCHES COMMENTS PAGE
@main.route('/promotioncomments/<int:promotion_pitch_id>', methods = ['GET','POST'])
@login_required
def promotionComments(promotion_pitch_id):
    '''
    View root page function that returns the promotion pitch comments page and its data
    '''

    promotion_pitch = Promotion.query.filter_by(id = promotion_pitch_id).first().promotion
    print(promotion_pitch)
    promotion_author = Promotion.query.filter_by(id = promotion_pitch_id).first().user.username
    print(promotion_author)
    promotion_postedDate = Promotion.query.filter_by(id = promotion_pitch_id).first().postedDate
    print(promotion_postedDate)
    promotion_likes = PromotionLikes.query.filter_by(promotion_pitch_id = promotion_pitch_id).count()
    print(promotion_likes)
    promotion_dislikes = PromotionDislikes.query.filter_by(promotion_pitch_id = promotion_pitch_id).count()
    print(promotion_dislikes)

    #Create an instance of the CommentForm class and name it comments_form
    comments_form = CommentForm()

    #The method returns True when the form is submitted and all the data has been verified by the validators
    if comments_form.validate_on_submit():
        #If True we gather the data from the form input fields
        comment = comments_form.comment.data

        #Create a new comment object and save it
        new_comment = PromotionComments(comment=comment, user=current_user, promotion_pitch_id=promotion_pitch_id )
        new_comment.save_promotionComment()

        return redirect(url_for('main.promotionComments',promotion_pitch_id=promotion_pitch_id))

    #Get all the Comments
    all_comments = PromotionComments.get_promotionComments(promotion_pitch_id)

    return render_template('promotion-comments.html', comments_form = comments_form, all_comments = all_comments, promotion_pitch_id = promotion_pitch_id, promotion_pitch = promotion_pitch, promotion_author = promotion_author, promotion_postedDate = promotion_postedDate, promotion_likes = promotion_likes, promotion_dislikes = promotion_dislikes)

#PROMOTION PITCHES UPVOTES
@main.route('/promotionlike/<int:id>', methods = ['GET', 'POST'])
def promotion_upvotes(id):
    promotion_upvotes = PromotionLikes.get_promotionlikes(id)

    valid_string = f'{current_user.id}:{id}'

    for promotion in promotion_upvotes:
        to_str = f'{promotion}'

        print(valid_string+" "+to_str)

        if valid_string == to_str:
            return redirect(url_for('main.promotion',id=id))
        else:
            continue

    new_promotion_upvote = PromotionLikes(user = current_user, promotion_pitch_id=id)
    new_promotion_upvote.save_promotionlike()

    return redirect(url_for('main.promotion',id=id))

#PROMOTION PITCHES DOWNVOTES
@main.route('/promotiondislike/<int:id>', methods = ['GET', 'POST'])
def promotion_downvotes(id):
    promotion_downvotes = PromotionDislikes.get_promotiondislikes(id)

    valid_string = f'{current_user.id}:{id}'

    for promotion in promotion_downvotes:
        to_str = f'{promotion}'

        print(valid_string+" "+to_str)

        if valid_string == to_str:
            return redirect(url_for('main.promotion',id=id))
        else:
            continue

    new_promotion_downvote = PromotionDislikes(user = current_user, promotion_pitch_id=id)
    new_promotion_downvote.save_promotiondislike()

    return redirect(url_for('main.promotion',id=id))

