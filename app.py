from flask import *

app = Flask(__name__)

@app.route('/')
def default():
    return redirect(url_for("home"))

@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
