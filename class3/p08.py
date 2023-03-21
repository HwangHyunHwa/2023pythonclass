for dan in range(2, 10):
    print('\n%d단: ' % dan, end = '')
    for num in range(1, 10) :
        print('%dx%d=%d ' % (dan, num, dan * num),end = '')
print('\n')
for num in range(1,10):
    for dan in range(2,10):
        print('%2dx%2d=%2d ' % (dan, num, dan * num), end = '')
    print('\n')
    