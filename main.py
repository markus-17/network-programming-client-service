from pydoc import cli
import requests

from Client import Client
from DataStore import DataStore, Restaurant
from settings import FOOD_ORDERING_HOSTNAME, FOOD_ORDERING_PORT


clients = {}

if __name__ == '__main__':
    restaurant_information = requests.get(f'http://{FOOD_ORDERING_HOSTNAME}:{FOOD_ORDERING_PORT}/menu').json()
    for restaurant in restaurant_information["restaurants_data"]:
        DataStore.RESTAURANTS[restaurant['restaurant_id']] = Restaurant(
            menu=restaurant['menu'],
            menu_items=restaurant['menu_items'],
            name=restaurant['name'],
            restaurant_id=restaurant['restaurant_id']
        )
    print(f'Client-Service acquired the Menu')

    for id in range(1, 4):
        clients[id] = Client(id)

    for client in clients.values():
        client.start()
