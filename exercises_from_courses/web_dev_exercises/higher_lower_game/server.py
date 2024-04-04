from flask import Flask
import random

app = Flask(__name__)

number = 0
hidden_number = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess the number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def number_guess(number):
    if number < hidden_number:
        return '<h1 style="color:red">Too low, try again!</h1>'
    elif number > hidden_number:
        return '<h1 style="color:purple">Too high, try again!</h1>'
    elif number == hidden_number:
        return '<h1 style="color:green">You found me!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
