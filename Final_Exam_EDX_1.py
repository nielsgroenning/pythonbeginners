def str_analysis(user_input):
    if user_input.isdigit() and int(user_input) > 99:
        print(user_input,' is a pretty big number')
    elif user_input.isdigit() and int(user_input) < 99:
        print(user_input, ' is a smaller number than expected')
    elif user_input.isalpha():
        print('\"'+ user_input +'\"'' is all alphabetical Characters')
    else:
        print("The input is a both alphanumeric and integeres")

while True:
    user_input = input('Please write a Word or an Integer: ')
    if user_input.isalpha():
        str_analysis(user_input)
        break
    elif user_input.isdigit():
        str_analysis(user_input)
        break
    else:
        print("You did not write a word or an integer.\nTry again")


