class Car:
    def __init__(self, model, year, seller, price):
        self.model = model
        self.year = year if isinstance(year, int) else ValueError("Year should be an integer")
        self.seller = seller
        self.price = price if isinstance(price, int) else ValueError("Price should be an integer")
        # self.status = "available"

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value if isinstance(value, int) else ValueError("Year should be an integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value if isinstance(value, int) else ValueError("Price should be an integer")

    # def mark_as_sold(self, buyer):
    #     self.status = "sold"
    #     self.buyer = buyer
    #     self.record_sale()

    # def mark_as_returned(self, return_reason=None):
    #     self.status = "returned"
    #     self.return_reason = return_reason
    #     self.record_return()
