import string

def ABC_files():
    for bukva in string.ascii_uppercase:
        open(bukva+".txt", "w")

ABC_files()