sum = 0
while True:
    user_input = input("Add integer to variable: ")
    if user_input.isdigit():
        sum = sum + int(user_input)
        print(sum)
    else:
        print('The sum is '+str(sum))
        break
