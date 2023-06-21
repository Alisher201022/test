from flask import Flask, render_template

app = Flask(__name__)
#
# @app.route("/contact")
# def contact():
#     name = "Alish"
#     age= "13"
#     return render_template("contact.html", name=name, age=age, title="not default")

@app.route("/")
def home():
    user = {
        "name": "Alish",
        "age": 13
    }
    return render_template("index.html", user=user)

@app.route("/contact")
def contact():
    user = {
        "name": "Alish",
        "age": 13
    }
    return render_template("contact.html", user=user)


@app.route("/profile")
def profile():
    user = {
        "name": "Alish",
        "age": 13
    }
    return render_template("profile.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)

