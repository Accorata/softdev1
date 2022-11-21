from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def load_main () :
    return render_template("main.html", test="hello")


if __name__ == "__main__":
    app.debug = True
    app.run()