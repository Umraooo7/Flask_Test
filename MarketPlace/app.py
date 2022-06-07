# from crypt import methods
import imp
from flask import Flask, jsonify
from requests import request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name':'My item',
            'price': 15.99
            }
        ]
    }
]

# Post to retrieve the data
app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# Get /store/<string:name>
app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return(jsonify(store))
    return jsonify(({'message':'store not found'}))

# POST method for items
app.route('store/<string:name>/item',method=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)



# GET method for items
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':stores['items']})
    return jsonify({'message':'store not found'})

app.run()