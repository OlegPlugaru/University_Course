fname = input('Enter File: ')
if len(fname) < 1 : fname = 'My_file.txt'
handle = open(fname)

dic = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:

        oldcount = dic.get(word,0)

        print(word,'old',oldcount)
        newcount = oldcount + 1
        dic[word] = newcount
        print(word,'new',newcount)


print(dic)