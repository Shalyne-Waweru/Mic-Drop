from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

# The UserMixin class implements 4 methods:-
# 1. is_authenticated() - Returns a boolean if a User is authenticated or not.,
# 2. is_active()- Checks if a user is allowed to authenticate,
# 3. is_anonymous()- Returns a boolean if a user is anonymous.
# 4. get_id()- Returns a unique identifier for User.

from flask_login import UserMixin
from . import login_manager

#Callback function that retrieves a user when a unique identifier is passed.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    emails = db.Column(db.String(255),unique = True,index = True)
    usernames = db.Column(db.String(255),unique = True,index = True)
    password_hashes = db.Column(db.String(255))

    #Define the relationship with the Pickup model.
    pickupLines = db.relationship('Pickup',backref = 'user',lazy = "dynamic")
    #Define the relationship with the Interview model.
    interviews = db.relationship('Interview',backref = 'user',lazy = "dynamic")
    #Define the relationship with the Promotion model.
    promotions = db.relationship('Promotion',backref = 'user',lazy = "dynamic")

    # #Define the relationship with the Comments model.
    # comments = db.relationship('Comments', backref='user', lazy='dynamic')

    #Create a write only class property password
    @property
    def password(self):
        #Block access to the password property
        raise AttributeError('You cannot read the password attribute')

    #Generate a password hash and pass it to the password_hashes column property to save to the database.
    @password.setter
    def password(self, password):
        self.password_hashes = generate_password_hash(password)

    #Create a method verify_password that takes in a password
    #It hashes it and compares it to the hashed password to check if they are the same.
    def verify_password(self,password):
        return check_password_hash(self.password_hashes,password)

    #Functions to append the pitches to their respective relationship columns
    def addPickupLine(self,pickupLine):
        self.pickupLines.append(pickupLine)
        db.session.add(self)
        db.session.commit()

    def addInterview(self,interviewPitch):
        self.interviews.append(interviewPitch)
        db.session.add(self)
        db.session.commit()

    def addPromotion(self,promotionPitch):
        self.promotions.append(promotionPitch)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.usernames}'

class Pickup(db.Model):

    __tablename__ = 'pickuplines'

    id = db.Column(db.Integer,primary_key = True)
    pickupLine = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the user who wrote the pickup line
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # #Define the relationship with the Comments Model.
    # pline_comments = db.relationship('Comments',backref = 'plinecomments',lazy = "dynamic")

    def save_pickup_line(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_pickup_lines(cls):
        pickupLines = Pickup.query.all()
        return pickupLines

class Interview(db.Model):

    __tablename__ = 'interviews'

    id = db.Column(db.Integer,primary_key = True)
    interview = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the user who wrote the interview pitch
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_interview(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_interviews(cls):
        interviews = Interview.query.all()
        return interviews

class Promotion(db.Model):

    __tablename__ = 'promotions'

    id = db.Column(db.Integer,primary_key = True)
    promotion = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the user who wrote the promotion pitch
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_promotion(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_promotions(cls):
        promotions = Promotion.query.all()
        return promotions

class Comments():

    # __tablename__ = 'comments'

    # id = db.Column(db.Integer,primary_key = True)
    # comment = db.Column(db.String)
    # postedDate = db.Column(db.DateTime,default=datetime.now)
    # #Create Foreign key column where we store the id of the Pickup Line to be commented on
    # pline_post_id = db.Column(db.Integer,db.ForeignKey("pickuplines.id"))
    # #Create Foreign key column where we store the id of the user that commented on the Pickup Line
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def get_comments(cls,id):
    #     comments = Comments.query.filter_by(pline_post_id=id).all()
    #     return comments

    all_comments = []

    def __init__(self,comment):
        self.comment = comment

    #Appends the comment object to a class variable all_comments that is an empty list. 
    def save_comment(self):
        Comments.all_comments.append(self)

    #Clears all the Items from the list
    @classmethod
    def clear_comments(cls):
        Comments.all_comments.clear()

    #Get all the Comments
    @classmethod
    def get_comments(cls):

        response = []

        for comment in cls.all_comments:
                response.append(comment)

        return response