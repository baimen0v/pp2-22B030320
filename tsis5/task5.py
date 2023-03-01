import re
task5 = re.compile(r'a.+b\Z')
result = task5.search(input())
print("correct") if result != None else print("not correct")