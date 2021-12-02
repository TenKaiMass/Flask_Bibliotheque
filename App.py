from os import name
from flask import Flask, render_template, jsonify
app = Flask(__name__)


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

# return render_template('layout.html', title='hello my app', name=names)


if __name__ == '__main__':
    app.run(debug=True)
