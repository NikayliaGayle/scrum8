"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for

Products=[["Face Wash","This product is suitable for oily skin. It contains Salicylic Acid which is a super ingredient for oil control and exfoliation.", '12.00' ,"/static/pics/facewash.jpg",0], 
              ["Moisturiser", "This product is suitable for all skin types. It contains Hyaluronic Acid which helps restore the skin barrier", '8.00',"/static/pics/moisturiser.png",1],
              ["Serum","This prodcut is suitable for all skin types. It contains Niacinamide which helps minimize pores and improves uneven skin tone", "10.00","/static/pics/serum.png",2],
              ["Sunscreen", "This product is stuitable for all skin types and colours. It is SPF 40 to protect your skin from the harmful rays of the sun", "25.00","/static/pics/sunscreen.jpg",3]]
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/products')
def view_products():
    return render_template('products.html', products=Products)

@app.route('/products/<int:product_id>')
def specific(product_id):
    prod=Products[product_id]
    return render_template('prod.html',product=prod)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
