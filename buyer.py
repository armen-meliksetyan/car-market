from car_market import CarMarket

car_market = CarMarket('car_market.json')

class Buyer:
    def __init__(self, person):
        self.person = person
        self.spent_money = 0
        self.bought_cars = []

    def buy_car(self, car):
        if self.person['money'] >= car['price']:
            self.person['money'] -= car['price']
            self.person['spent_money'] += car['price']
            if car not in self.person['bought_cars']:
                self.person['bought_cars'].append(car)
                seller = car_market.get_seller_by_name(car['seller'])
                if seller:
                    seller['sold_cars'].append(car)
                    seller['money'] += car['price']
            car_market.update_buyer(self.person)  
            car_market.remove_car(car)  
            car_market.save_data()
            return True
        return False

    def return_car(self, car):
        self.person['money'] += car['price']
        self.person['spent_money'] -= car['price']
        self.person['bought_cars'].remove(car)
        seller = car_market.get_seller_by_name(car['seller'])
        seller['money'] -= car['price']
        seller['sold_cars'].remove(car)
        car_market.data['cars'].append(car)
        car_market.update_buyer(self.person) 
        car_market.save_data()