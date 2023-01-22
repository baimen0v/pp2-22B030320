# type() function show the data type of variable
a = "Hello World"	#str	
b = 20	#int	
c = 20.5	#float	
d = 1j	#complex	
e = ["apple", "banana", "cherry"]	#list	
e = ("apple", "banana", "cherry")	#tuple	
f = range(6)	#range	
g = {"name" : "John", "age" : 36}	#dict	
h = {"apple", "banana", "cherry"}	#set	
i = frozenset({"apple", "banana", "cherry"})  #frozenset	
j = True	#bool	
k = b"Hello"	#bytes	
l = bytearray(5)	#bytearray	
m = memoryview(bytes(5))	#memoryview	
n = None	#NoneType	
print(type(a))
print(type(b))
print(type(c))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
