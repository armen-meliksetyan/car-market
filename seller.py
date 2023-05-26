import car_market

class Seller:
    def __init__(self, person):
        self.person = person
        self.sold_cars = []

    def sell_car(self, car):
        self.sold_cars.append(car)
        car_market.save_data()
