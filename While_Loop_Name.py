familiar_name = ''
while True:
    familiar_name = input("Please indicate a familiar name: ")
    if familiar_name.isalpha() == True:
        print("You typed\n"+ familiar_name)
        break
    else:
        print("Try again") 
    


