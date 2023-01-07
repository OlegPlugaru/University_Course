import re

handle = open('mbox.txt')
for line in handle:
    line = line.rstrip()
    if re.search('From:',line) :
        print(line)