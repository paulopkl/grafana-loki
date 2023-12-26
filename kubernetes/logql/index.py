import requests
import random
import time

URL = "http://localhost/produto"
list_produtos = []

def populate_list():
    global products_list
    products_list = []
    for item in get_all():
        products_list.append(item["id"])
    print()

def get_all():
    r = requests.get(url = URL)
    return r.json()

def get_by_id(id):
    r = requests.get(url = URL + "/" + str(id))
    populate_list()
    return r.json()

def add_product(product):
    r = requests.delete(url = URL + "/?id=" + str(id))
    populate_list()
    return r

def delete(id):
    r = requests.delete(url = URL + "/?id=" + str(id))
    populate_list()
    return r

populate_list()

while(True):
    n = random.randint(1, 1000)

    if(n % 5 == 0 and len(products_list) > 0):
        delete(random.randint(1, len(products_list) - 1))

    if(n % 2 == 0):
        add_product({"nome": "Produto", "preco": 1000, "categoria": ""})

    get_all()

    print("Executed")
    print(len(products_list))
    time.sleep(1)
