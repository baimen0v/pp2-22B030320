a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
c = 33
if c > a:
  print("c is greater than a")
elif a == c:
  print("a and c are equal")

x = 201
y = 32
if x > y:
  print("x is greater than y")
elif x == y:
  print("x and y are equal")
else:
  print("y is greater than x")

d = 333
g = 14
if d > g: print("d is greater than g")
print("D") if d > g else print("G")

e = 332
f = 332
print("E") if e > f else print("=") if e == f else print("F")

h = 200
i = 33
j = 500
if h > i and j > h:
  print("Both conditions are True")
if h > i or h > j:
    print("At least one condition is true")

k = 41
if k > 10:
  print("Above ten,")
  if k > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
