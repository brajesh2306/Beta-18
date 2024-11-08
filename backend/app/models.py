class FoodConsumption:
    def __init__(self, food_item, quantity_consumed, quantity_wasted, date):
        self.food_item = food_item
        self.quantity_consumed = quantity_consumed
        self.quantity_wasted = quantity_wasted
        self.date = date

class Inventory:
    def __init__(self, item_name, quantity, expiry_date):
        self.item_name = item_name
        self.quantity = quantity
        self.expiry_date = expiry_date
