thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

print(len(thisdict))

x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

thisdict["year"] = 2020
print(thisdict)

thisdict.update({"year": 2055})
print(thisdict)

thisdict.update({"color": "red"})
print(thisdict)

thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)