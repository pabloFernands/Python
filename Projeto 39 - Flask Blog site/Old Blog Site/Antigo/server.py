from flask import Flask, render_template
import datetime

app = Flask(__name__)

def load_css():
    return

today = datetime.datetime.now().year
print(today)


@app.route("/")
def home():
    return render_template("index.html", date=today)


if __name__ == "__main__":
    app.run(debug=True)
