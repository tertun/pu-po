from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_homepage.html')

@app.route('/France_homepage.html')
def france():
    return render_template('France_homepage.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/Ghana_homepage.html')
def Ghana():
    return render_template('Ghana_homepage.html')

@app.route('/Korea_homepage.html')
def Korea():
    return render_template('Korea_homepage.html')

@app.route('/USA_homepage')
def USA():
    return render_template('USA_homepage.html')

if __name__ == '__main__':
    app.run(port = 2000,debug=True)