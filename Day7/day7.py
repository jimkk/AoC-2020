import re

with open('input.txt', 'r') as file:
    data = file.readlines()

data = [re.findall(r'([\w ]+) contain ([\w0-9 ,]+)', a)[0] for a in data]
print(data[0])
rules = ['\'%s\'(%s).' % (a[0], a[1]) for a in data]
print(rules[0])
