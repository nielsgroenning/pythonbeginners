tries = 4
color = 'red, orange, yellow, green, blue, indigo, violet"'
while tries > 0:
    user_input = input("Guess the color in a Rainbow: ")
    if user_input.lower() in color == True:
        print("Right Guess")
        break
    else:
        tries = tries - 1
        print("You have",tries,"tries left")
