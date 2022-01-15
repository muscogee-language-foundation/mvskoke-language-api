from flask import Flask, request, abort
from flask_restful import Resource, Api
from marshmallow import Schema, fields, post_load
from search import search, SearchQuery

# arguments for the search query
class SearchQuerySchema(Schema):
    query = fields.Str(required=True)

    # deserializing the object
    @post_load
    def make_object(self, data, **kwargs):
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
        return search(searchObject)

@app.route('/')
def index():
    return '<p>Welcome to the Mvskoke Language Api.  To search, try the endpoint /search?query=[myquery]</p>'

api.add_resource(SearchAPI, '/search', endpoint = 'search')

if __name__ == "__main__":
    app.run(host='0.0.0.0')