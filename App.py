import json
from flask import Flask, render_template, jsonify, request
import random
app = Flask(__name__)


@app.route('/')
def home():
    return 'Rien à Voir Ici'


@app.route('/api/books', methods=['GET'])
def index():

    # cree un livre
    book = [
        {
            'id': 1,
            'titre': 'un titre',
        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]
    book = json.dumps(book)
    return jsonify(book)
    # search_term = request.args.get(book)
    # return search_term
    # return render_template('layout.html', title='hello my app', book=book)


@app.route('/api/books/id', methods=['GET'])
def getBookByid():

    book = [
        {
            'id': 1,
            'titre': 'un titre',

        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]

    livreAlea = random.randint(0, 1)
    print(livreAlea)
    if book[livreAlea]['id'] == 1:
        #book = json.dumps(book)
        return jsonify(book[livreAlea])
    if book[livreAlea]['id'] == 2:
        #book = json.dumps(book)
        return jsonify(book[livreAlea])


@app.route('/api/books/titre', methods=['GET'])
def getBookByTitle():

    book = [
        {
            'id': 1,
            'titre': 'un titre',

        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]

    livreAlea = random.randint(0, 1)
    print(livreAlea)
    if book[livreAlea]['titre'] == 'un titre':
        return jsonify(book[livreAlea])
    if book[livreAlea]['titre'] == 'un autre titre random':
        return jsonify(book[livreAlea])


@app.route('/api/books/catalogue', methods=["POST", "GET"])
def getBooks():
    with open("books.json", "r") as read_file:
        data = json.load(read_file)
    # aleaBook = random.randint(0, len(data))
    # data = json.dumps(data[aleaBook])
    if request.method == "POST":
        livre = request.form["idortitle"]
        for i in range(0, len(data)):
            if data[i]['isbn'] == livre or data[i]['title'] == livre:
                data = json.dumps(data[i])
                return jsonify(data)
            else:
                return render_template('erreurBook.html', title='Fail')

                # return jsonify(data)
    else:
        return render_template('catalogue.html', title='Catalogue')


if __name__ == '__main__':
    app.run(debug=True)
