a = int(input('A. Add a number: '))
b = int(input('B. Add another number: '))
c = int(input('C. Add a third number: '))
if a < b and a < c:
    print('A is the smallest number')
elif b < c:
    print('B is the smallest number')
else:
    print('C is the smallest number')