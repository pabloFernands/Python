from flask import Flask, render_template
import requests

app = Flask(__name__)
GENDER_ENDPOINT = "https://api.genderize.io"
AGE_ENDPOINT = "https://api.agify.io"


@app.route("/")
def home():
    return "Put a name in the URl. Ex: /pablo"


@app.route("/<name>")
def guess(name):
    parameter = {
        "name": name
    }
    response_gender = requests.get(GENDER_ENDPOINT, params=parameter)
    new_gender = response_gender.json()
    gender = new_gender["gender"]
    #print(gender)
    response_age = requests.get(AGE_ENDPOINT, params=parameter)
    new_age = response_age.json()
    age = new_age["age"]
    return render_template("page.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
