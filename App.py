from flask import Flask
App=Flask(__name__)

@App.route('/')
def home():
    return "Home"

@App.route('/about' )
def about():
    return "about1"

if __name__=="__main__":
    App.run(debug=True)