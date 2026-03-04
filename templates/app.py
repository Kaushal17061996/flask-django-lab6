from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Flask!</h1>"

@app.route("/hello/<name>")
def hello_name(name):
    return render_template("hello.html", name=name)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("hello_name", name=name))
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)