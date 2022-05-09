from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm, LoginForm
from flask_login import login_user,logout_user,login_required
from .. import db
from . import auth

#LOGIN PAGE
@auth.route('/login',methods=['GET','POST'])
def login():
    # # Create the form instance and pass it into our template
    login_form = LoginForm()

    if login_form.validate_on_submit():
        #Search for a user from our database with the email we receive from the form
        user = User.query.filter_by(emails = login_form.emails.data).first()

        #Confirm that the password entered matches with the password hash stored in the database.
        if user is not None and user.verify_password(login_form.password.data):
            #The login_user function records the user as logged for that current session
            login_user(user,login_form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Email or Password')

    return render_template('auth/login.html',login_form = login_form)

#SIGN UP PAGE
@auth.route('/register',methods = ["GET","POST"])
def register():
    # Create the form instance and pass it into our template
    signup_form = RegistrationForm()

    if signup_form.validate_on_submit():
        #Create a new user from the User model and pass in the email,username and password.
        user = User(emails = signup_form.emails.data, usernames = signup_form.usernames.data,password = signup_form.password.data)
        #Add the new user to the session
        db.session.add(user)
        #Commit the session to add the user to our database.
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',signup_form = signup_form)

#LOGOUT PAGE
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))