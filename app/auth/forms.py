from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter Username',validators = [DataRequired()])
    password = PasswordField('Enter Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    #Custom validators
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')