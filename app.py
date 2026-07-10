from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    blog_name = "Flask Blog"
    owner = "Bilal Asghar"
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


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "404.html",
        blog_name="Flask Blog"
    ), 404


if __name__ == "__main__":
    app.run(debug=True)