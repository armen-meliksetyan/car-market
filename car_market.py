import json

class CarMarket:
    def __init__(self, data_file):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = file.read()
                if data:
                    self.data = json.loads(data)
                else:
                    self.data = {
                        'sellers': [],
                        'buyers': [],
                        'cars': []
                    }
        except FileNotFoundError:
            self.data = {
                'sellers': [],
                'buyers': [],
                'cars': []
            }

    def update_buyer(self, buyer):
        for i, existing_buyer in enumerate(self.data['buyers']):
            if existing_buyer['name'] == buyer['name']:
                self.data['buyers'][i] = buyer
                break

    def remove_car(self, car):
        self.data['cars'] = [c for c in self.data['cars'] if c['model'] != car['model']]

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file)

    def add_seller(self, seller):
        self.data['sellers'].append(seller.person.__dict__)
        self.save_data()

    def add_buyer(self, buyer):
        if 'buyers' not in self.data:
            self.data['buyers'] = []
        self.data['buyers'].append(buyer.person.__dict__)
        self.save_data()

    def get_buyer_by_name(self, name):
        for buyer in self.data['buyers']:
            if buyer['name'] == name:
                return buyer
        return None
    
    def get_car_by_model(self, model):
        for car in self.data['cars']:
            if car['model'] == model:
                return car
        return None

    def add_car(self, car, seller_name):
        seller = self.get_seller_by_name(seller_name)

        if seller is None:
            print("There is no seller with this name.")
            return

        car = {
            'model': car.model,
            'year': car.year,
            'price': car.price,
            'seller': seller_name
        }
        self.data['cars'].append(car)
        self.save_data()

    def get_seller_by_name(self, name):
        for seller in self.data['sellers']:
            if seller['name'] == name:
                return seller
        return None

    def get_cars_by_seller(self, seller_name):
        cars = []
        for car in self.data['cars']:
            if car['seller'] == seller_name:
                cars.append(car)
        return cars
