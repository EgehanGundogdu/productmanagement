from backend.application import app, collection

from flask import jsonify, request


@app.route('/')
def hello():

    return jsonify({
        'results': list(collection.find({}))
    })


@app.route('/add-product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({
            'status': 201
        })
    return jsonify({
        'status': 400,
        'message': 'Bad request'
    })
