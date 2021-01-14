from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

users = {
    'users_list' :
    [
        {
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id' : 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method =='GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username :
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if search_job:
                    if user['name'] == search_username and user['job'] == search_job:
                        subdict['users_list'].append(user)
                else:
                    if user['name'] == search_username:
                        subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method =='POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        #resp.status_code = 200
        #optionally, you can always set a response code.
        # 200 is the default code for a normal response
        return resp

#@app.route('/users/<id>', methods=['GET', 'DELETE'])
#def get_user(id):
#    if request.method == 'GET':
#        if id :
#            for user in users['users_list']:
#                if user['id'] == id:
#                    return user
#            return ({})
#        return users
#    elif request.method == 'DELETE':
#        for user in users['users_list']:
#            if user['id'] == id:
#                users['users_list'].remove(user)
#        resp = jsonify(success=True)
#        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id:
        if request.method == 'GET':
            for user in users['users_list']:
                if user['id'] == id:
                    return user
                else:
                    resp = jsonify({"Msg": "User not found with provided ID"}), 404
            return resp
        elif request.method == 'DELETE':
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    resp = jsonify(), 204
                    return resp
                else:
                    resp = jsonify({"Msg": "User not found with provided ID"}), 404
            return resp
        return users

@app.route('/')
def hello_world():
    return 'Hello World'