def adding_report(report):
    total = 0
    items = ''
    while True:
        user_input = input('Enter an integer or'+'\"''Q''\"'+':'+'\n')
        if user_input.isdigit(): 
            items = (items+'\n'+user_input)
            user_input = int(user_input)
            total = total + user_input
        elif user_input =='Q':
                if report =='T':
                    print('Total:'+'\n'+str(total))
                    break
                if report =='A':
                    print('Items:'+str(items)+'\n')
                    print('Total:'+'\n'+str(total))
                    break
        else:
                print('Input invalid')

a_or_t = input('Choose Report type (A) or (T): ')
adding_report(a_or_t)