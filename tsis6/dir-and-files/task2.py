import os

def existence(path):
    try:
        os.path.exists(path)
        print("exist\n")
    except:
        print("doesn't exist\n")

def readability(path):
    try:
        open(path, "r")
        print("readable\n")
    except:
        print("not readable\n")

def writability(path):
    try:
        open(path, "w").close()
        print("writable\n")
    except:
        print("not writable\n")

def executability(path):
    try:
        os.startfile(path)
        print("executable\n")
    except:
        print("not executable\n")


file = input("Enter your path: ")


existence(file)
readability(file)
writability(file)
executability(file)