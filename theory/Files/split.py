fhand = open('mbox-large.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    count += 1
    print(count, words[2])