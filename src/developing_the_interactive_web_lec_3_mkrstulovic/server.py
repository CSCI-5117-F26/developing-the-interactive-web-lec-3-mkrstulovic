from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    global guestbook
    return render_template("index.html", guestbook=guestbook)

""" @app.route('/hi', methods=['GET'])
def hello_world():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name) 
 """
guestbook = []

@app.route('/guestbook', methods=['POST'])
def add_to_guestbook():
   global guestbook
   if request.form.get("name"):
      guestbook.append(request.form.get("name"))
   return render_template("index.html", guestbook=guestbook)