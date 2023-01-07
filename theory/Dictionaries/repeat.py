fname = input('Enter file: ')
if len(fname) < 1:
    fname = "My_file.txt"
handle = open(fname)

dic = dict()
for line in handle:
     line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        # print(word)
        # print('**', word, dic.get(word, -99))
        # If the key is not there the count is zero
        # oldcount = dic.get(word, 0)
        # print(word, 'old', oldcount)
        # newcount = oldcount + 1
        # dic[word] = newcount
        # idiom : retrieve/create/update/counter
        dic[word] = dic.get(word, 0) + 1
        # print(word, 'new', dic[word])

        # if word in dic:
        #     dic[word] = dic[word] + 1
            # print('**Existing**')
        # else:
        #     dic[word] = 1
            # print('**NEW**')
        # print(word, dic[word])

# print(dic)

# now we want to find the most common word
largest = -1
theword = None
for key, value in dic.items():
    # print(key, value)
    if value > largest:
        largest = value
        theword = key      #capture/remember the word that was largest
print('Done', theword, largest)