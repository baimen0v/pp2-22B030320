a = 5
b = "John"
print(a)
print(b)

c = 4 # c is of type int
c = "Sally" # now c is of type string
print(c)

d = str(3) # d will be '3'
e = int(3) # e will be 3
f = float(3) # f will be 3.0
print(d)
print(e)
print(f)



i,j,k = "Orange", "Banana", "Cherry"
print(i)
print(j)
print(k)

fruits = ["apple", "banana", "orange"]
l, m, n = fruits
print(l)
print(m)
print(n)

o = "Python"
p = "is"
q = "awesome"
print(o, p, q)
print(o + p + q)

r = "cool"

def myfunc():
  print("Python is " + r)

myfunc()



s = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + s)

myfunc()

print("Python is " + s)



def myfunc():
  global t
  t = "meow"

myfunc()

print("Python is " + t)

