import sys

class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= self.MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print(f"The disc '{dvd.title}' has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            return True
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def total_cost_with_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")
        return round(self.total_cost() * (100 - percent) / 100, 2)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("=== CART ===")
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item.title} - {item.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
