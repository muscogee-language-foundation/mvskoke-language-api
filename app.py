from flask import Flask, request, abort
from flask_restful import Resource, Api
from marshmallow import Schema, fields, post_load

# basic Search class
class SearchQuery:
    def __init__(self, query):
        self.query = query

# arguments for the search query
class SearchQuerySchema(Schema):
    query = fields.Str(required=True)

    # deserializing the object
    @post_load
    def make_user(self, data, **kwargs):
        return SearchQuery(**data)

app = Flask(__name__)
api = Api(app)
schema = SearchQuerySchema()

# define the api, validate, return results
class SearchAPI(Resource):
    def get(self):
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        searchObject = schema.load(request.args)
        return do_search(searchObject)

@app.route("/")
def index():
    return "<h1 style='color:green'>Welcome to the Mvskoke Language API!</h1>"

api.add_resource(SearchAPI, '/search', endpoint = 'search')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# do the actual search
def do_search(searchObject: SearchQuerySchema):
    return "you searched for "+searchObject.query
