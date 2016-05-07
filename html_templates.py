#!usr/bin/python


from flask import Flask,render-template
app=Flask(__name__)

@app.route('/profile/<name>')
#app routes to the profile page
def profile(name):
    return render_template("profile.html",name=name)


#initializes the server
if __name__=="__main__":
    app.run()
