def adding_report(report = 'T'):
    while True:
        total = 0
        items= ''
        user_input = input('Enter an integer or'+'\"''Q''\"'+':'+'\n')
        if user_input.isdigit():
            items=(items+'/n'+user_input)
            user_input=int(user_input)
            total=total+user_input
        elif user_input =='Q':
            if user_input =='A':
                print('Items:')
                print(items)
                print('Total:'+'\n'+total)
            if user_input =='T':
                print('Total:'+total)
                break
        else:
            print('The input is invalid')


a_or_t = input('Choose Report type (A) or (T): ')
adding_report(a_or_t)