from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/eventDetails')
def eventDetails():
    return render_template('eventDetails.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/setting')
def setting():
    return (render_template('admin-setting.html'))

@app.route('/profile')
def profile():
    return (render_template('admin/profile.html'))

@app.route('/booking')
def booking():
    return (render_template('admin/admin-booking.html'))

@app.route('/customers')
def customers():
    return (render_template('admin/admin-customers.html'))

@app.route('/ad-events')
def ad_events():
    return (render_template('admin/ad-events.html'))

@app.route('/createevent')
def createEvent():
    return (render_template('admin/createevent.html'))

@app.route('/editevent')
def editevent():
    return (render_template('admin/editevent.html'))

@app.route('/searchevent')
def searchevent():
    return (render_template('admin/ticket-purchase/searchevent.html'))

@app.route('/purchaseticket')
def purchaseTicket():
    return (render_template('admin/ticket-purchase/purchase-ticket.html'))

if __name__ == "__main__":
    app.run(debug=True)