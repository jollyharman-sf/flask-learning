from crypt import methods
from time import strftime
from flask import render_template, request, redirect
from datetime import datetime
from app import app

@app.template_filter("clean_date")
def clean_date(dt):
    return strftime("%d %b %Y")


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    #string
    my_name = "Julian"

    #integer
    my_age = 17

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    #class
    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        
        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    
    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        url="https://github.com/Julian-Nash/learning-flask.git"
    )

    #function
    def repeat(x, qty=1):
        return x * qty

    #custom filter object
    date = datetime.utcnow()

    my_html = "<h1>This is some html </h1> "

    sus = "<script> alert ('you have have been hacked') </script>"
    

    return render_template("public/jinja.html", my_name=my_name, my_age=my_age, langs=langs, friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, repeat=repeat, my_remote=my_remote, date=date, my_html=my_html, sus=sus)

@app.route("/about")
def about():
    return "<h1 style= 'color: red' > About !!</h1>"

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        
        req = request.form
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]

        print(username, email, password)

    return render_template("public/signup.html")

# key value pair arbitrary data is made, key: mitsuhiko and value: name, bio and twitter
users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creater of of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):

    print(username)

    return render_template("public/profile.html")