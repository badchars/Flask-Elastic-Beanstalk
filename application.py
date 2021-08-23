import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def api_home():
        return "paths '/api/v1/changeUserSettings'"

# A route to return all of the available entries in our admin log.
@app.route('/api/v1/changeUserSettings', methods=['POST'])
def api_cards():
    if 'username' in request.args:
        name = request.args['username']
    else:
        return "Error: No username field provided. Please specify an accountType,name,firstname and address."
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name field provided. Please specify an accountType,name,firstname and address."
    if 'firstname' in request.args:
        name = request.args['firstname']
    else:
        return "Error: No firstname field provided. Please specify an accountType,name,firstname and address."
    if 'address' in request.args:
        name = request.args['address']
    else:
        return "Error: No address field provided. Please specify an accountType,name,firstname and address."
    if 'accountType' in request.args:
        type = request.args['accountType']
    else:
        return "Error: No type field provided. Please specify an accountType,name,firstname and address. The type can be either user or reader"
    if type == 'admin':
        return "Good job!! Flag: (21384324-03240324)"
    else:
        return "account settings saved"

app.run(host="0.0.0.0",port="5006")
