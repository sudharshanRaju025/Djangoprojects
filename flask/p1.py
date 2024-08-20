from flask import Flask, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP server
app.config['MAIL_PORT'] = 587  # SMTP port
app.config['MAIL_USE_TLS'] = True  # Use TLS
app.config['MAIL_USE_SSL'] = False  # Do not use SSL
app.config['MAIL_USERNAME'] = 'bsudharshan404@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = ''  # Your email password
# app.config['MAIL_DEFAULT_SENDER'] = @gmail.com'  # Default sender
app.config['MAIL_DEFAULT_SENDER'] = ('DigitalLync', 'sudharshanb025@gmail.com')  # Default sender

mail = Mail(app)

@app.route('/send_message')
def send_message():
    msg = Message("Hello",
                  recipients=["sudharshanb025@gmail.com"])
    msg.body = "This is a test message sent from a Flask application."
    
    # Specify the path to your file
    file_path = 'image.jpg'
   # Ensure the file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fp:
            msg.attach("image.jpg", "image/jpg", fp.read())
    
    mail.send(msg)
    return "Message sent with attachment!"

if __name__ == '__main__':
    app.run(debug=True)