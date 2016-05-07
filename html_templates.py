#!usr/bin/python


from flask import Flask,render-template
app=Flask(__name__)

@app.route('/profile/<name>')
#app routes to the index page
def index(name):
    return render_template("profile.html",name=name) 
