#!usr/bin/python

app=Flask(__name__)

#@ signifies a decorator that is used to wrap a function
#and modify its behaviour.

@app.route('/')
def index():
    return "this is my homepage"

@app.route('/sample')
def sample():
    return "<h2> This is a sample </h2>"

@app.route('/profile/<username>')
def profile (username):
    return "Hey there %s" %username

if __name__=="__main__":
    app.run()
