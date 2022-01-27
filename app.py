from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security_3 import authenticate, identity
from resources.user_3 import UserRegister
from resources.item_3 import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/Stores')

api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True