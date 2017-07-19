from flask import Flask
app = Flask('oruko-server')

@app.route('/api/v1/items/<int:item_id>')
def get_item(item_id):
    return r'{"name": "server_item", "id": "%d", "description": "Some boring stuff..."}' % item_id
