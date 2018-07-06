from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]= True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")