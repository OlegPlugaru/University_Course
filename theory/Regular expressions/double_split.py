

data = open('mbox.txt')

for line in data:
    line = line.rstrip()
    if line.startswith("From"):

        words = line.split()
        email = words[1]
        pieces = email.split('@')
        print(pieces[1])
