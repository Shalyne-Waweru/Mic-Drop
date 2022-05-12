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
    email = db.Column(db.String(255),unique = True,index = True)
    username = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    #Define the relationship with the Pickup model.
    pickupLines = db.relationship('Pickup',backref = 'user',lazy = "dynamic")
    #Define the relationship with the Interview model.
    interviews = db.relationship('Interview',backref = 'user',lazy = "dynamic")
    #Define the relationship with the Promotion model.
    promotions = db.relationship('Promotion',backref = 'user',lazy = "dynamic")
    #Define the relationship with the Comments model.
    comments = db.relationship('PickupComments', backref='user', lazy='dynamic')
    #Define the relationship with the PickupLikes model.
    pickuplikes = db.relationship('PickupLikes', backref = 'user', lazy = 'dynamic')
    #Define the relationship with the PickupDislikes model.
    pickupdislikes = db.relationship('PickupDislikes', backref = 'user', lazy = 'dynamic')
    #Define the relationship with the InterviewComments model.
    interview_comments = db.relationship('InterviewComments', backref='user', lazy='dynamic')
    #Define the relationship with the InterviewLikes model.
    interviewlikes = db.relationship('InterviewLikes', backref = 'user', lazy = 'dynamic')
    #Define the relationship with the InterviewDislikes model.
    interviewdislikes = db.relationship('InterviewDislikes', backref = 'user', lazy = 'dynamic')

    #Create a write only class property password
    @property
    def password(self):
        #Block access to the password property
        raise AttributeError('You cannot read the password attribute')

    #Generate a password hash and pass it to the password_hash column property to save to the database.
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    #Create a method verify_password that takes in a password
    #It hashes it and compares it to the hashed password to check if they are the same.
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

#PICKUP LINES
class Pickup(db.Model):

    __tablename__ = 'pickuplines'

    id = db.Column(db.Integer,primary_key = True)
    pickupLine = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the user who wrote the pickup line
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    #Define the relationship with the Comments Model.
    pline_comments = db.relationship('PickupComments',backref = 'plinecomments',lazy = "dynamic")
    #Define the relationship with the PickupLikes model.
    pickuplikes = db.relationship('PickupLikes', backref = 'plinelikes', lazy = 'dynamic')
    #Define the relationship with the PickupDislikes model.
    pickupdislikes = db.relationship('PickupDislikes', backref = 'pickupdislikes', lazy = 'dynamic')
    
    def save_pickup_line(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_pickup_lines(cls):
        pickupLines = Pickup.query.all()
        return pickupLines

class  PickupComments(db.Model):

    __tablename__ = 'pickupcomments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the Pickup Line to be commented on
    pickup_id = db.Column(db.Integer,db.ForeignKey("pickuplines.id"))
    #Create Foreign key column where we store the id of the user that commented on the Pickup Line
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comments(cls,id):
        comments = PickupComments.query.filter_by(pickup_id=id).all()
        return comments

class PickupLikes(db.Model):
    __tablename__ = 'pickuplikes'

    id = db.Column(db.Integer,primary_key=True)
    pickup_id = db.Column(db.Integer,db.ForeignKey("pickuplines.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pickuplike(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pickuplikes(cls,id):
        plinelikes = PickupLikes.query.filter_by(pickup_id=id).all()
        return plinelikes

class PickupDislikes(db.Model):
    __tablename__ = 'pickupdislikes'

    id = db.Column(db.Integer,primary_key=True)
    pickup_id = db.Column(db.Integer,db.ForeignKey("pickuplines.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pickupdislike(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pickupdislikes(cls,id):
        plinedislikes = PickupDislikes.query.filter_by(pickup_id=id).all()
        return plinedislikes

class Interview(db.Model):

    __tablename__ = 'interviews'

    id = db.Column(db.Integer,primary_key = True)
    interview = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the user who wrote the interview pitch
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    #Define the relationship with the  InterviewComments Model.
    interview_comments = db.relationship('InterviewComments',backref = 'interviewcomments',lazy = "dynamic")
    #Define the relationship with the InterviewLikes model.
    interviewlikes = db.relationship('InterviewLikes', backref = 'interviewlikes', lazy = 'dynamic')
    #Define the relationship with the InterviewDislikes model.
    interviewdislikes = db.relationship('InterviewDislikes', backref = 'interviewdislikes', lazy = 'dynamic')

    def save_interview(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_interviews(cls):
        interviews = Interview.query.all()
        return interviews

class  InterviewComments(db.Model):

    __tablename__ = 'interviewcomments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the Interview Pitch to be commented on
    interview_pitch_id = db.Column(db.Integer,db.ForeignKey("interviews.id"))
    #Create Foreign key column where we store the id of the user that commented on the Interview Pitch
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def save_interviewComment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_interviewComments(cls,id):
        comments = InterviewComments.query.filter_by(interview_pitch_id=id).all()
        return comments

class InterviewLikes(db.Model):
    __tablename__ = 'interviewlikes'

    id = db.Column(db.Integer,primary_key=True)
    interview_pitch_id = db.Column(db.Integer,db.ForeignKey("interviews.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_interviewlike(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_interviewlikes(cls,id):
        interviewlikes = InterviewLikes.query.filter_by(interview_pitch_id=id).all()
        return interviewlikes

class InterviewDislikes(db.Model):
    __tablename__ = 'interviewdislikes'

    id = db.Column(db.Integer,primary_key=True)
    interview_pitch_id = db.Column(db.Integer,db.ForeignKey("interviews.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_interviewdislike(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_interviewdislikes(cls,id):
        interviewdislikes = InterviewDislikes.query.filter_by(interview_pitch_id=id).all()
        return interviewdislikes

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
