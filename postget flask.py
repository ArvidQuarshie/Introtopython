#!usr/bin/python
#checks to see what http methods you are using

from flask import Flask,request
app=Flask(__name__)

@app.route('/')
#app routes to the index page
def index():
    return "the method used was" %request.method
#app routes to the about page
@app.route("/about",method=['GET','POST'])
def example():
    if request.method=='POST':
        return "You are using POST"
    else:
        return "You are using GET"








#initializes the server
if __name__=="__main__":
    app.run()
