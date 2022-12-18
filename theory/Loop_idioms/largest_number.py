largest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

largest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if largest is None:
        largest = value
    elif largest < value :
        largest = value
    print(largest, value)
print('After', largest)