import os

def existence(path):
    if os.path.exists(path) is True:
        print("exist")
        print("filename of the path:")
        print(os.path.basename(path))
        print("directory name of the path:")
        print(os.path.dirname(path))
    else:
        print("doesn't exist")