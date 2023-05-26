from car_market import CarMarket
from buyer import Buyer
from seller import Seller
from car import Car
from person import Person

car_market = CarMarket('car_market.json')

buyer = None
seller = None

while True:
    command = input("Enter a command: ")

    if command == "list":
        print("List of cars for sale:")
        for car in car_market.data['cars']:
            print(car)

    elif command == "buy":
        buyer_name = input("Buyer name: ")
        buyer = Buyer(CarMarket.get_buyer_by_name(car_market, buyer_name))
        if buyer:
            model = input("Enter the model of the car you want to buy: ")
            car_to_buy = None
        else:
            print("No buyer created. Use 'create_buyer' command to create a buyer.")

        car_to_buy = CarMarket.get_car_by_model(car_market, model)
        if car_to_buy:
            if buyer.buy_car(car_to_buy):
                car_market.data['cars'].remove(car_to_buy)
                Buyer.buy_car(buyer, car_to_buy)
                print(f"You have successfully bought the {car_to_buy['model']}.")
            else:
                print("You do not have enough money to buy the car.")
        else:
            print("The car you entered is not available for sale.")
        
        
    elif command == "return":
        buyer_name = input("Buyer name: ")
        buyer = Buyer(CarMarket.get_buyer_by_name(car_market, buyer_name))
        if buyer:
            model = input("Enter the model of the car you want to return: ")
            car_to_return = None
    
            for car in buyer.person['bought_cars']:
                if car['model'] == model:
                    car_to_return = car
                    break
            if car_to_return is None:
                print("The car you entered is either not found or already returned.")
            else:
                buyer.return_car(car_to_return)
                print(f"You have successfully returned the {car_to_return['model']}.")
        else:
            print("No buyer created. Use 'create_buyer' command to create a buyer.")
            continue
        

    elif command == "create_buyer":
        name = input("Enter the buyer's name: ")
        surname = input("Enter the buyer's surname: ")
        city = input("Enter the buyer's city: ")
        money = int(input("Enter the buyer's money: "))
        buyer = Buyer(Person(name, surname, city, money))
        car_market.add_buyer(buyer)
        print("buyer successfully created")

    elif command == "create_seller":
        name = input("Enter the seller's name: ")
        surname = input("Enter the seller's surname: ")
        city = input("Enter the seller's city: ")
        seller = Seller(Person(name, surname, city))
        car_market.add_seller(seller)
        print("seller successfully created")

    elif command == "add_car":
        seller_name = input("Seller name: ")
        if car_market.get_seller_by_name(seller_name):
            car_to_buy = None
            model = input("Enter the car's model: ")
            year = int(input("Enter the car's year: "))
            price = int(input("Enter the car's price: "))
            car = Car(model, year, seller, price)
            car_market.add_car(car, seller_name)
        else:
            print("No seller created. Use 'create_seller' command to create a seller.")

    elif command == "exit":
        break

    else:
        print("Invalid command. Please try again.")
