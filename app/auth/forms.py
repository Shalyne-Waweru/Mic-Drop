from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    emails = StringField('Enter Email Address',validators=[DataRequired(),Email()])
    usernames = StringField('Enter Username',validators = [DataRequired()])
    password = PasswordField('Enter Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired()])
    style={ 'style': 'background-color: black; color: white; width:430px; margin-top: 20px; '}
    submit = SubmitField('SIGN UP',render_kw=style)

    #Custom validators
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    emails = StringField('Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])

    checkbox_style={ 'style': 'width:15px; height:15px;'}
    remember = BooleanField('Remember me?',render_kw=checkbox_style)

    style={ 'style': 'background-color: black; color: white; width:430px; margin-top: 20px; '}
    submit = SubmitField('LOGIN',render_kw=style)