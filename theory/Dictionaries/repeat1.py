fname = input("Enter filename: ")
if len(fname) < 1:
    fname = "My_file.txt"
handle = open(fname)

dic = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1

largest = -1
theword = None
for key, value in dic.items():
    if value > largest:
        largest = value
        theword = key
print('Done', theword, largest)
