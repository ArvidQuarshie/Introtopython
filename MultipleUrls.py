#!usr/bin/python

from flask import Flask,render_template
app=Flask(__name__)

 # "using multiple urls in one python script"
# we have mapped the two decorators to the function render_template()
@app.route("/<")
@app.route("/"<user>)


#users none by default
def index(user=None):
#the render template function takes in the user name that is passed from the
    #script and passes it on to the user.html which is a template

#user=user refers to the name of the user when they log in
    return render_template("user.html",user=user)
#initializes the server
if __name__=="__main__":
    app.run()
