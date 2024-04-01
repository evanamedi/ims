import random
import time

class Shop:
    def __init__(self, initial_books):
        self.books = initial_books
        self.price = 50
        self.sales = 0

    def update(self):
        if self.books < 20:
            self.books += 50
            self.price += 2
        elif self.books < 50:
            self.price += 1
        else:
            self.price = max(10, self.price - 1)

    def sell_book(self, weather):
        if self.books > 0 and (weather != 'rainy' or random.random () < 0.5):
            self.books -= 1
            self.sales += self.price
            return self.price
        else:
            return 0

class Customer:
    def __init__(self):
        self.money = 100

    def buy_book(self, shop, weather):
        price = shop.sell_book(weather)
        if self.money >= price:
            self.money -=price
            return True
        else:
            return False

    def is_broke(self):
        return self.money <= 0

def simulate():
    shop = Shop(100)
    customers = [Customer() for _ in range(5)]
    start_time = time.time()
    week = 0
    while time.time() - start_time < 30:
        for day in range(30):
            weather = 'sunny' if random.random() < 0.7 else 'rainy'
            if random.random() < 0.99:
                customers.append(Customer())
            for customer in customers[:]:
                if random.random() < 0.99:
                    customer.buy_book(shop, weather)
                if customer.is_broke():
                    customers.remove(customer)
                shop.update()
                print(f"Week {week + 1}, {weather.capitalize()}: Sales = {shop.sales}, Books left = {shop.books}, Customers = {len(customers)}")
                time.sleep(.1)
            week += 1
        

simulate()