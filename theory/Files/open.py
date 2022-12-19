xfile = open('mbox.txt')

for cheese in xfile :
    print(cheese)

fhandle = open('mbox-large.txt')
count = 0

for line in fhandle :
    count = count + 1
print('Line count:',count)

