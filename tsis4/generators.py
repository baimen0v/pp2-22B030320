#1
def squaree(n):
    for i in range(n):
        yield i**2

n=int(input())
print(list(squaree(n)))
#2
def even(N):
    for i in range(1,N+1):
        if i%2==0:
            yield i

n=int(input())
print(*list(even(n)),sep=", ")
#3
def iterates(eee):
    for i in range(eee):
        if i%3 == 0 and i%4 == 0:
            yield i

n = int(input())
print(list(iterates(n)))
#4
def squares(a,b):
    for i in range(a,b):
        yield i**2

a=int(input())
b=int(input())
for num in squares(a,b):
    print(num)
#5
def returns(n):
    for i in range(n,0,-1):
        yield i

n=int(input())
for zz in returns(n):
    print(zz)