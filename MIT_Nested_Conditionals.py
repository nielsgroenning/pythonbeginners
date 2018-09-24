x = int(input('Please add a number: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisable by 2 and 3')
    else:
        print('Divisable by 2 and not 3')
elif x%3 == 0:
    print('Divisable by 3 and not 2')


