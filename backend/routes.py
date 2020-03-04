from backend.application import app, collection

from flask import jsonify, request


@app.route('/api/getproducts')
def hello():
    results = [i.pop('_id') for i in list(collection.find({}))]
    return jsonify({
        'results': results
    })


@app.route('/api/add-product', methods=['POST'])
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


@app.route('/sell-product', methods=['GET', 'POST'])
def sell_proudct():
    pass
