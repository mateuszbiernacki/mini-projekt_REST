import requests
from kcals import Product
URL = "http://127.0.0.1:2137/"


def get_kcal(number):
    r = requests.get(url=URL+'/kcals/get-num/'+number+'/')
    print('Url: ' + str(r.url))
    print('Kod statusu: ' + str(r.status_code))
    print('Odpowiedz: ' + str(r.text))


def get_counter():
    r = requests.get(url=URL+'/kcals/get-counter/')
    print('Url: ' + str(r.url))
    print('Kod statusu: ' + str(r.status_code))
    print('Odpowiedz: ' + str(r.text))


def get_all():
    r = requests.get(url=URL+'/kcals/get-all/')
    print('Url: ' + str(r.url))
    print('Kod statusu: ' + str(r.status_code))
    print('Odpowiedz: \n' + str(r.text))


def post_product(name, kcal):
    p = Product()
    p.add(name, kcal)
    r = requests.post(url=URL+'/kcals/post/', json=p.list[0], headers={'Content-Type': 'application/json'})
    print('url: ' + str(r.url))
    print('Kod statusu:  ' + str(r.status_code))
    print('Wyslano:  ' + str(r.text))


if __name__ == "__main__":
#    get_kcal('1')
#    get_counter()
    get_all()
    post_product('Pizza Hut Pepperoni Pizza', 291)
#    get_count()
    get_all()