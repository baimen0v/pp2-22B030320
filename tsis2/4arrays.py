cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
a = len(cars)
print(a)
for x in cars:
  print(x)

cars.append("Honda")
cars.pop(0)
cars.remove("Volvo")
print(cars)
