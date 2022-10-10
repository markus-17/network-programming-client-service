import random
import threading
from urllib import response

import requests

from DataStore import DataStore
from settings import FOODS_PER_ORDER_COUNT, FOOD_ORDERING_HOSTNAME, FOOD_ORDERING_PORT


class Client(threading.Thread):
    def __init__(self, client_id):
        super().__init__()
        self.client_id = client_id

    def run(self):
        restaurant_ids = [random.choice(list(DataStore.RESTAURANTS.keys())) for _ in range(FOODS_PER_ORDER_COUNT)]
        rest_and_food_id = [(restaurant_id, random.choice(list(DataStore.RESTAURANTS[restaurant_id].menu.keys()))) for restaurant_id in restaurant_ids]
        rest_and_food_id.sort()

        body = {'client_id': self.client_id}    
        orders = []
        for restaurant_id, food_id in rest_and_food_id:
            create_new = True

            for order in orders:
                if order['restaurant_id'] == restaurant_id:
                    order['items'].append(food_id)
                    create_new = False

            if create_new:
                orders.append({
                    'restaurant_id': restaurant_id,
                    'items': [food_id],
                })
    
        body['orders'] = orders

        response = requests.post(url=f"http://{FOOD_ORDERING_HOSTNAME}:{FOOD_ORDERING_PORT}/order", json=body)

        print(response.json())
