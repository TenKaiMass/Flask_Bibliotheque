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

    return jsonify(book)
    # search_term = request.args.get(book)
    # return search_term
    # return render_template('layout.html', title='hello my app', book=book)


@app.route('/api/books/<int:id>', methods=['GET'])
def getBookByid(id):

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

    # livreAlea = random.randint(0, 1)
    if id == 1:
        return jsonify(book[0])
    if id == 2:
        # book = json.dumps(book)
        return jsonify(book[1])
    else:
        return render_template('erreurBook.html', title='Fail')


@app.route('/api/books/<titre>', methods=['GET'])
def getBookByTitle(titre):

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

    if titre == 'un titre':
        return jsonify(book[0])
    if titre == 'un autre titre random':
        return jsonify(book[1])
    else:
        return render_template('erreurBook.html', title='Fail')


@app.route('/api/books/catalogue', methods=["POST", "GET"])
def getBooks():
    with open("./books.json", "r") as read_file:
        data = json.load(read_file)
    # aleaBook = random.randint(0, len(data))
    # data = json.dumps(data[aleaBook])
    if request.method == "POST":
        livre = request.form["idortitle"]
        for i in range(0, len(data)):
            if data[i]['isbn'] == livre or data[i]['title'] == livre:
                return render_template('search.html', title='searchRes', data=data[i])
            else:
                return render_template('erreurBook.html', title='Fail')

                # return jsonify(data)
    else:
        return render_template('catalogue.html', title='Catalogue')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# from typing import Optional

# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
