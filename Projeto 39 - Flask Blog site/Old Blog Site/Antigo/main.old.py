from flask import Flask
import random

app = Flask(__name__)

def make_bold(function):
    def this_function():
        return f'<b><h1>{function()}</h1></b>'
    return this_function

@app.route("/")
@make_bold
def hello_world():
    return "Hello, guess the number in the Url. Ex: /5"

#right_number = random.randint(1,9)
right_number = 2
print(right_number)

@app.route("/<number>")
def find_number(number):
    number = int(number)
    if number == right_number:
        return "Você acertou!\
        <p><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></p>"
    elif number < right_number:
        return "Você errou!\
        Tente outro numero maior.\
        <p><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></p>"
    else:
        return "Você errou!\
        Tente outro numero menor.\
        <p><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g'></p>"

if __name__ == "__main__":
    app.run(debug=True)