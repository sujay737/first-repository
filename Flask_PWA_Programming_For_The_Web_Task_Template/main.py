from flask import Flask, render_template, request, redirect, url_for
import database_manager as dbHandler

app = Flask(__name__)

# --- helper for form handling with optional redirect ---


def handle_form(template_name, redirect_to=None):
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        if username and email:
            dbHandler.insert_data(username, email)
            if redirect_to:
                return redirect(url_for(redirect_to))
            return render_template(template_name, message="Data submitted!")
    return render_template(template_name)


@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    return handle_form("index.html")


@app.route("/index_copy1.html", methods=["GET", "POST"])
def index_copy1():
    return handle_form("index_copy1.html")


@app.route("/index_copy2.html", methods=["GET", "POST"])
def index_copy2():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")

        if username and email:
            # store info (comment out if you don’t have dbHandler yet)
            try:
                dbHandler.insert_data(username, email)
            except Exception:
                pass

            # 🚩 THIS is what sends the browser to menu.html
            return redirect(url_for("menu"))

    # if GET or missing fields, just render the form again
    return render_template("index_copy2.html")


@app.route("/index_copy3.html", methods=["GET", "POST"])
def index_copy3():
    return handle_form("index_copy3.html")


# --- menu page ---
@app.route("/menu.html")
def menu():
    return render_template("partials/menu.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


