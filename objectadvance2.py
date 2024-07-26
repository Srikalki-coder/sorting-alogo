class order_food:
    objectall = []
    access = "I can acess from child class"
    def __init__(self, food_type: str, price = 100) -> None:
        assert price > 0
        self.food = food_type
        self.__price =  price
        print(f"{self.food}, {self.__price}")
        order_food.objectall.append(self)
    def __repr__(self) -> str:
        return f"{self.food}, {self.price}"
    def __discount(self, discount):
        return self.__price - self.__price * discount/100
    @classmethod
    def classmethodd(cls):
        print("I can also access from class level")
    @property
    def price(self):
        return self.__price
    """  @price.setter
    def price(self, value):
        self.___price = value
        return value """

""" class child(order_food):
    def __init__(self, food_type, price=100) -> None:
        super().__init__(food_type, price) """

object1 = order_food("curry", 250)
print(object1)




























