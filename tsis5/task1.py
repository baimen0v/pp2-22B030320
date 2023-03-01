import re
task1 = re.compile(r'ab*')
result = task1.search(input())
print("correct") if result != None else print("not correct")