
price_boeg_100 = 150
price_boeg_80 = 75
price_leguster_100 = 25
price_leguster_150 = 50
available = 'bøg, leguster'

while True: 
        haek_type = input('Hvilken Hæk vil du købe (Bøg eller Leguster)? ')
        if haek_type.lower() in available:
            print('Du har valgt',haek_type)
            print()
            meter = int(input('Hvor mange meter skal du bruge? '))
            hoejde = int(input('Hvor høje skal planterne være (100, 80 eller 180 cm) ? '))
            if haek_type.lower() == 'bøg' and hoejde == 100:
                print('Din hæk koster:',meter*price_boeg_100,' Kr.')
                print()
                break
            elif haek_type.lower() == 'bøg' and hoejde == 80:
                print('Din hæk koster:',meter*price_boeg_80,' Kr.')
                break
            elif haek_type.lower() == 'leguster' and hoejde == 100:
                print('Din hæk koster:',meter*price_leguster_100,' Kr.')
                break
            elif haek_type.lower() == 'leguster' and hoejde == 150:
                print('Din hæk koster:',meter*price_leguster_100,' Kr.')
                break
            elif hoejde > 150:
                print('Vi har desværre ikke',haek_type,'på',int(hoejde),' meter')
        else:
            print('Vi har desværre ikke',haek_type,'i vores butik')