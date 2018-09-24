#Guess a the bird.
bird = 'parrot, dove, pigeon'
guess = input('Guess a Bird: ')
guess_count = 3

if bird.lower() not in guess:
    print('Wrong Guess. You have',int(guess_count-1),'tries left')
    guess_2 = input('2nd guess.Guess a Bird: ')
    if guess_2.lower() not in bird:
        print('Wrong guess',int(guess_count-2),'try left')
        guess_3 = input('Third Guess. Guess a Bird: ')
        if guess_3.lower() not in bird:
            print('You failed and have used all',int(guess_count),'tries')
        else:
            print('Congratulations you passed on third try')
    else: 
        print('Rigth Second time')
else:
    print('Right First Time')