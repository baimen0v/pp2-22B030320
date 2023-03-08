import os

path = input("Enter your path: ")
list = list(map(int, input("Enter your list: ").split()))

writtenFile = open(path, "a")
writtenFile.write(str(list))
writtenFile.close()