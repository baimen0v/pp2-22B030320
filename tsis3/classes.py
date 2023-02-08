#1
class Upper:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string = input()
    def PrintString(self):
        print((self.string).upper())


obj = Upper()
obj.getString()
obj.PrintString()

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self , length):
        self.length = length

    def area(self):
        return (self.length**2)
    
a = Square(8)
print(a.area())

#3
class Shape:
    def area(self):
        return 0

class Rectagle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

rect = Rectagle(10, 20)
print(rect.area())

#4
import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def show(self):
        print (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self,x1,y1,x2,y2):
        return math.sqrt((x2 - x1)**2+(y2 - y1)**2)
 
coord = Point()
coord.show()
coord.move(12,12)
print(coord.dist(1,1,5,5))

#5
class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, deposit_):
        self.balance+=deposit_
    def withdraw(self, withdraw):
        if withdraw<=self.balance:
            self.balance -= withdraw
        else:
            print("little money")
    def show(self):
        print(self.balance)

Worker = bank("John", 1000)
Worker.deposit(350)
Worker.show()

Worker.withdraw(300)
Worker.show()

#6
def is_prime(num):
    if num == 1:
        return False
    if num > 1:
        for j in range(2, int(num/2)+1):
            if (num % j) == 0:
                return False
        return True
    else:
        return True

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

prime = filter(lambda x: is_prime(x), my_list)
print(list(prime))
