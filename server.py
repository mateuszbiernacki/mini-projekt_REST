import flask
from kcals import Product

from flask import request
product = Product()
app = flask.Flask(__name__)


@app.route('/kcals/get-num/<string:prod>/', methods=['GET'])
def get_kcal(prod):
    buff = product.get_kcal(prod)
    return buff


@app.route('/kcals/get-counter/', methods=['GET'])
def get_counter():
    counter = product.count()
    return "Liczba produktów: "+str(counter)


@app.route('/kcals/get-all/', methods=['GET'])
def get_all():
    s = product.display_all()
    return s


@app.route('/kcals/post/', methods=['POST'])
def post_product():
    p = request.json
    product.add(p['name'], int(p['kcal']))
    return p


if __name__ == "__main__":
    product.add('Broccoli', 38)
    product.add('Chicken broth', 86)
    product.add('Nachos', 306)
    app.run(port=2137)