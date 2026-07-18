from flask import Flask
from flask import render_template
from forms import ContactForm


from forms import LoginForm
from forms import RegistrationForm
from models import User,Role

from extensions import db



app = Flask(__name__)

app.config["SECRET_KEY"] = "my-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home_page():
    blog_name = "Flask Blog"
    owner = "Arslan Zafar"
    total_posts = 3

    posts = [
        "Introduction to Flask",
        "Understanding Routes",
        "Learning Jinja2 Templates"
    ]

    return render_template(
        "index.html",
        blog_name=blog_name,
        owner=owner,
        total_posts=total_posts,
        posts=posts
    )


@app.route("/about")
def about_page():
    blog_name = "Flask Blog"
    owner = "Arslan Zafar"
    return render_template(
        "about.html",
        blog_name=blog_name,
        owner=owner
    )


@app.route("/contact", methods=["GET", "POST"])
def contact_page():

    form = ContactForm()

    if form.validate_on_submit():

        print(form.name.data)

        print(form.email.data)

        print(form.message.data)

    return render_template(

        "contact.html",

        blog_name="Flask Blog",

        owner = "Arslan Zafar",

        form = form
    )

@app.route("/login", methods=["GET", "POST"])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():

        print("Username:", form.username.data)

        print("Password:", form.password.data)

        print("Remember Me:", form.remember_me.data)

    return render_template(
        "login.html",
        form=form
    )


@app.route("/register", methods=["GET", "POST"])
def register_page():

    form = RegistrationForm()

    if form.validate_on_submit():

        print("Username:", form.username.data)

        print("Email:", form.email.data)

        print("Password:", form.password.data)

    return render_template(
        "register.html",
        form=form
    )

@app.route("/create-user")
def create_user():

    user = User(
        username="arslan",
        email="zafar@gmail.com"
    )

    db.session.add(user)

    db.session.commit()

    return "User Created Successfully"

@app.route("/users")
def users():

    users = User.query.all()

    result = ""

    for user in users:
        result += f"{user.username} - {user.email}<br>"

    return result

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    