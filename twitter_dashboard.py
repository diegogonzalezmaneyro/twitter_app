#Start the code here

#import libs
from flask import Flask, render_template, make_response

#init app
app = Flask(__name__)

#define differents pages to work
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response(render_template('error.html'), 404)
    return response


if __name__ == '__main__':
    app.run(debug=True)
