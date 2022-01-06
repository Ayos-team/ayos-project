from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import session


app = Flask(__name__)

# Set the secret key to some random bytes.
# Keep this really secret!
app.secret_key = b'w33uwueed@!@'

@app.route('/')
def index():
    return render_template('home.html', page="Home")


@app.route('/services')
def services():
    return render_template('services.html', page="Services")


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")

@app.route('/chat')
def chat():
    return render_template('chat.html', page="Chat")


@app.route('/contactdetails')
def contactdetails():
    return render_template('contactdetails.html', page="Contact Details")


@app.route('/Map')
def map():
    return render_template('Map.html', page="Map")

@app.route('/myprofile')
def myprofile():
    return render_template('myprofile.html', page="My Profile")


@app.route('/myservices')
def myservices():
    return render_template('myservices.html', page="My Services")


@app.route('/notifications')
def notifications():
    return render_template('notifications.html', page="Notifications")

@app.route('/paymentmethod')
def paymentmethod():
    return render_template('paymentmethod.html', page="Payment Method")


@app.route('/rewards')
def rewards():
    return render_template('rewards.html', page="Rewards")

@app.route('/serviceprovider')
def serviceprovider():
    return render_template('serviceprovider.html', page="Service Provider")

@app.route('/datechoosing')
def datechoosing():
    return render_template('datechoosing.html', page="Date Choosing")

@app.route('/confirmed')
def confirmed():
    return render_template('confirmed.html', page="Confirmed")
