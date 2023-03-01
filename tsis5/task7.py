import re
task7 =input()
def snake_camel(text):
    snake=re.findall('[a-z]+',text)
    camel=""
    for i in snake:
        camel+=i[0].upper()+i[1:len(i)]
    return camel

print(snake_camel(task7))
    