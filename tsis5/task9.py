import re
task9 = input()
print(re.sub(r"(\w)([A-Z])", r'\1 \2', task9))
