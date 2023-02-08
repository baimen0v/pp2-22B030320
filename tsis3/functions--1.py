#1
ounces = 28.3495231
def converter(grams):
    result=float(grams)/float(ounces)
    return result
print(converter(input()))

#2
def temperature(F):
    return int((5 / 9) * (int(F) - 32))
print((temperature(input())))

#3
def solve(numheads, numlegs):
    chickens = 0
    rabbits = 0
    chickens = (4*numheads - numlegs)/2
    rabbits = numheads - chickens
    return {"chickens": chickens, "rabbits": rabbits}

print(solve(43, 84))

#4
def isPrime(check_num):
    if check_num==1:
        return False
    if check_num > 1:
        for j in range(2, int(check_num/2)+1):
            if (check_num % j) == 0:
                return False
        return True
    else:
        return True

def filter_prime(my_list):
    result = []
    for iter in my_list:
        if isPrime (int(iter)):
            result.append((iter))
    return result
            

my_list = input().split(' ')
print((filter_prime(my_list)))

#5
from itertools import permutations
def permut(str):
    return list(permutations(str, len(str)))

print(permut(input()))

#6
def reverser(str):
    my_list = list(str.split())
    result = ""
    for word in my_list[::-1]:
        result += word+' '
    return result
print(reverser(input()))

#7
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1,3,1]))

#8 
pi=3.14
def volume(radius):
    return 4/3*pi*radius**2
print(volume(input()))

#9
def unique(nums):
    res = dict()
    for item in nums:
        res[item] = 0
    for item in nums:
        res[item] += 1
    output = []
    for key,value in res.items():
        if value == 1:
            output.append(key)
    return output


print(unique([1,1,2,3,4,4,21,42,4]))

#11
def palindrome(str1):
    str2 = str1[::-1]
    return str2 == str1

print(palindrome(input()))

#12
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([4,9,7])

#13
import random

name = input("Hello! What is your name?\n")

number = random.randint(1,20)
counter = 0
print(f"Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.")

while(True):
    a = int(input())
    counter += 1
    if a > number:
        print("Your guess is too high. \nTake a guess.")
    elif a < number:
        print("Your guess is too low. \nTake a guess.")
    elif a == number:
        print(f"Good job, {name}! You guessed my number in {counter} guesses!")
        break