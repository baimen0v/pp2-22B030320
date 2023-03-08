import os

def existence(path):
    try:
        os.path.exists(path)
        return True
    except:
        return False

current_path = os.getcwd()
file_name = input("Enter your filename: ")
path = os.path.join(current_path, file_name)

if existence(path)==True:
    os.remove(path)
    print(f"file {file_name} was deleted\n")
else:
    print("doesn't exist\n")