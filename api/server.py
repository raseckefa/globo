from flask import Flask 
from flask_restful import Api
from flask_cors import CORS

from Controller.Cards import Cards, CardsByid, CardsBytag, CardsByAny
from Controller.Tags import Tags, TagsByid 

app = Flask(__name__)
cors = CORS(app, resources={r"/cards/*": {"origins": "*"}})
cors = CORS(app, resources={r"/tags/*": {"origins": "*"}})
api = Api(app)

api.add_resource(Cards, '/cards')
api.add_resource(CardsByid, '/cards/<id>')
api.add_resource(CardsBytag, '/cards/tag/<id>')
api.add_resource(CardsByAny, '/cards/any/<texto>')

api.add_resource(Tags, '/tags')
api.add_resource(TagsByid, '/tags/<id>') 

if __name__ == '__main__': 
    app.run()
