from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = "shalyne.waweru@student.moringaschool.com"

    #Create a Message instance and pass in the subject, the sender_email and the recipient.
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)

    #We use the send method of the mail instance and pass in the email instance.
    mail.send(email)