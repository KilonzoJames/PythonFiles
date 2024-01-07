import os
from flask_mail import Mail
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
 
app = Flask(__name__)

# After 'Create app'
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["SECURITY_CONFIRMABLE"] = True

mail = Mail(app)

def send_simple_message():
    pass

send_simple_message()