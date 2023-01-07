handle = open('mbox.txt')
for line in handle:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
