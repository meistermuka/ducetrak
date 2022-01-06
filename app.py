from http import HTTPStatus

from chalicelib.handlers.produce_handler import ProduceHandler

from chalice import Chalice, Response

app = Chalice(app_name='ducetrak')


@app.route('/')
def index():
    return {'ping': 'pong'}

@app.route('/produce')
def produce() -> Response:
    return ProduceHandler().get_produce()

@app.route('/type')
def produce_type():
    return {'produce': 'type'}

@app.route('/price')
def price():
    return {'produce': 'price'}

@app.route('/user')
def user():
    return {'user': 'user'}

@app.route('/location')
def location():
    return {'location': 'location'}

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
