from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PickupLineForm(FlaskForm):

    pickupLine = TextAreaField('Pickup Line', validators=[DataRequired()])
    style={ 'style': 'background-color: black; color: white; '}
    submit = SubmitField('SUBMIT',render_kw=style)

class InterviewForm(FlaskForm):

    interview = TextAreaField('Interview Pitch', validators=[DataRequired()])
    style={ 'style': 'background-color: black; color: white; '}
    submit = SubmitField('SUBMIT',render_kw=style)

class PromotionForm(FlaskForm):

    promotion = TextAreaField('Promotion Pitch', validators=[DataRequired()])
    style={ 'style': 'background-color: black; color: white; '}
    submit = SubmitField('SUBMIT',render_kw=style)

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment', validators=[DataRequired()])
    style={ 'style': 'background-color: black; color: white; '}
    submit = SubmitField('SUBMIT',render_kw=style)