import re
task10 = input()
step1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', task10)
step2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', step1).lower()
print(step2)