print("------------------------------")
a = 5
b = "John"
print(a)
print(b)
print("------------------------------")
c = 4 # c is of type int
c = "Sally" # now c is of type string
print(c)
print("------------------------------")
d = str(3) # d will be '3'
e = int(3) # e will be 3
f = float(3) # f will be 3.0
print(d)
print(e)
print(f)

print("-----------------------------")

i,j,k = "Orange", "Banana", "Cherry"
print(i)
print(j)
print(k)
print("------------------------------")
fruits = ["apple", "banana", "orange"]
l, m, n = fruits
print(l)
print(m)
print(n)
print("------------------------------")
o = "Python"
p = "is"
q = "awesome"
print(o, p, q)
print(o + p + q)
print("------------------------------")
r = "cool"

def myfunc():
  print("Python is " + r)

myfunc()

print("------------------------------")

s = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + s)

myfunc()

print("Python is " + s)

print("------------------------------")

def myfunc():
  global t
  t = "meow"

myfunc()

print("Python is " + t)
print("------------------------------")
