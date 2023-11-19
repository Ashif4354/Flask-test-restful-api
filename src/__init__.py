from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return jsonify({'hello':'world'})
    
#create some more test resources
class Test(Resource):
    def get(self):
        return jsonify({'test':'test'})

class Test2(Resource):
    def get(self):
        return jsonify({'test2':'test2'})

api.add_resource(Home, '/')
api.add_resource(Test, '/test')
api.add_resource(Test2, '/test2')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 840, debug = True)

