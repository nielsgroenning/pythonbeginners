
def rainbow_color(string_parameter):
    if color.lower() =='R' or 'r':
        print('You Choose RED')
    elif color.lower() =='O' or 'o':
        print('You choose ORANGE')
    elif color.lower() =='Y' or 'y':
        print('You choose YELLOW')
    elif color.lower() =='G' or 'g':
        print('You choose GREEN')
    elif color.lower() =='B' or 'b':
        print('You choose BLUE')
    elif color.lower() =='I' or 'i':
        print('You choose INDIGO')
    elif color.lower() =='V' or 'v':
        print('You choose VIOLET')
    else:
        print('No match')                            
                        

color = input('Choose color (ROYGBIV): ')
rainbow_color(color)