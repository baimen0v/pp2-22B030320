import re
task2 = re.compile(r'ab{2,3}[^b]')
result = task2.search(input())
print("correct") if result != None else print("not correct")