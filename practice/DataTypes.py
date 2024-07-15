# Data Types Practice 
# String 
color = "green"
print(color)
print(type(color))

car1 = "Toyota"
car2 = "Audi"
car1and2 = car1 + " " + car2 
print(car1and2)
print(type(car1and2))

# Integer
time = 10
velocity = 7
distance = time * velocity
print(str(distance) + "M")
print(type(distance))

# Float 
time1 = 15 
distance1 = 40 
velocity1 = distance1 / time1 
velocity1 = int(velocity1) # 정수형으로 변환
print(velocity1)
print(type(velocity1))

# Boolean 
a = 5
b = 7 
c = 9 
total = a + b 
if total > c:
    print(True) 
else:
    print(False)

min = 65
grade = 77
passingstatus = True 
if grade < min:
    passingstatus = False
else:
    passingstatus = True
print(passingstatus)
