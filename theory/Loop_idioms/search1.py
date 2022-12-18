print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print('Large number', value)
print('After')

found = False
print ('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        print(found, value)
        print('I got it, here is your value:',value)
        break
    print(found, value)

print('After', found)