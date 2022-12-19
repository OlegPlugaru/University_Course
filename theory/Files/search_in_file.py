fhand = open('mbox-large.txt')
count = 0
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') :
        count += 1
        print(count,line)
