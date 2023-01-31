a = 1
while a < 6: 
    a +=1
    print(a)
b = 1
while b < 8:
    print(b)
    if b == 3:
        break
    b +=1

c = 0
while c < 10:
    c +=1
    if c == 4:
        continue
    print(c)

d = 1
while d < 12:
    print(d)
    d +=1
else: print("d is no longer less than 12")