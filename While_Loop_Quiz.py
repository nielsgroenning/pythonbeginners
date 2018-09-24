tries = 3
answer = 'Copenhagen'

while tries > 0:
    answer_1 = input("Capital of Denmark? ")
    if answer_1.lower() == answer.lower():
        print('Correct.\nGood Job !')
        points = 10
        break
    elif answer_1 != answer:
        tries = tries - 1
        print('You have ',tries,'tries left\n')
    else:
        print("Try again") 

        

