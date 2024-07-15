class MyCar:
    amount = 5
x = MyCar()
print(x.amount)

class MyCarCollection:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color 
y = MyCarCollection("BMW", "Yellow")
print(y.brand)
print(y.color)