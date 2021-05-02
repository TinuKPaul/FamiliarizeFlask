from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
    {"id": 0,
     "author": "Auth0",
     "language": "English",
     "title": "Book0"
     },
    {"id": 1,
     "author": "Auth1",
     "language": "English",
     "title": "Book1"},
    {"id": 2,
     "author": "Auth2",
     "language": "English",
     "title": "Book2"}
]


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == "GET":
        if len(book_list) > 0 :
            return jsonify(book_list)
        else:
            return 'Nothing to Return', 404
    elif request.method == "POST":

        new_id = book_list[-1]['id'] + 1
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']

        book_list.append({"id": new_id,
        "author": new_author,
        "language": new_language,
        "title": new_title})

        return jsonify(book_list), 201


@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book_operations(id):
    if request.method == 'GET':
        for book in book_list:
            if book['id'] == id:
                return jsonify(book) , 201
    elif request.method == 'PUT':
        for book in book_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                return jsonify(book), 201

    elif request.method == 'DELETE':
        for index,book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(index)
                return jsonify(book_list), 201


if __name__ == "__main__":
    app.run()
