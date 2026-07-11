from flask import Flask
from flask import render_template
from forms import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "my-secret-key"

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
    return render_template("about.html")


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

        form = form
    )

if __name__ == "__main__":
    app.run(debug=True)
    