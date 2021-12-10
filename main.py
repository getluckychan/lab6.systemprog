import re

names = []

with open('rezult.txt', 'r') as f_input:
    for line in f_input:
        if len(line) > 1:
            names.append(re.match(r'(.*?):\s*?(\d+)\s*?', line).groups())


for name, mark in sorted(names, key=lambda x: float(x[1]), reverse=True):
    print("{}: {}".format(name, mark))


