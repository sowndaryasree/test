from flask import Flask
app = Flask(__name__)   # lowercase

@app.route('/home')
def home():
    return "Home"

@app.route('/about')
def about():
    return "about1"

if __name__ == "__main__":
    app.run(debug=True)
