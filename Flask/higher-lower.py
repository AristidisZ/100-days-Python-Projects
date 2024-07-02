from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1 style='text-align: left'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif'>"


random_integer = random.randint(0, 9)
print(random_integer)


@app.route('/<int:number>')
def guess(number):
    if number < random_integer:
        return "<h1 style='text-align: left'>Too Low</h1>" \
               "<img src='https://media2.giphy.com/media/IevhwxTcTgNlaaim73/200.webp?cid=790b761" \
               "1tqy5s2pvi6a42pdiblijblmkwxjjacorozmi4q4k&ep=v1_gifs_search&rid=200.webp&ct=g'>"
    elif number > random_integer:
        return "<h1 style='text-align: left'>Too high</h1>" \
               "<img src='https://media4.giphy.com/media/IdaC0lMrci4vu/200.webp?cid=790b7611r52xcz" \
               "eqhc12vjfgl4lx7ohe5xeic7wmzcvb81pb&ep=v1_gifs_search&rid=200.webp&ct=g'>"
    else:
        return "<h1 style='text-align: left'>Congratulation</h1>" \
               "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm9yc3hsbHdjdGNyYWtsZW9iaGh5OGU0ZG" \
               "9rNGphOWdsYjRrYTR2byZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/yoJC2GnSClbPOkV0eA/200.webp'>"


if __name__ == "__main__":
    app.run(debug=True)
