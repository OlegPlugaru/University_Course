fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'Myfile.txt'
handle = open(fname)

dic = dict()
place_count = 0
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # idiom: retrieve/create/update counter
        dic[word] = dic.get(word, 0) + 1

# print(dic)

# x = sorted(dic.items())
# print(x[:5])

temp = list()
for k, v in dic.items():
    # print(k, v)
    newtuple = (v, k)
    temp.append(newtuple)

# print('Flipped', temp)

temp = sorted(temp, reverse=True)
# print('Sorted', temp[:5])

for v, k in temp[:5]:
    place_count += 1
    print(str(place_count) + ". - ", k, v)

