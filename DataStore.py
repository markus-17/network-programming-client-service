from dataclasses import dataclass


@dataclass
class Restaurant:
    name: str
    menu_items: int
    menu: list[dict]
    restaurant_id: int


class DataStore:
    RESTAURANTS = {}
