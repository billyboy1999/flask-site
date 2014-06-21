import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("base.html", name="Home", content="Blah, blah, blah!")

@app.route('/games/')
def games():
    return render_template("base.html", name="Games", content="Testicles")

@app.route('/french/')
def french():
    return render_template("base.html", name="French", content="Le Penis")

@app.route('/contact/')
def contact():
    return render_template("base.html", name="Contact", content="willpoo")