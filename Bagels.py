from random import randint, shuffle
def Bagels():
    while(True):
        print('1.Start game \n2.Rules \n3.Exit')
        choice = int(input('\nEnter your choice: '))
        match choice:
            case 1:
                Num = list(str(randint(100, 1000)))
                for i in range(7):
                    while(True):
                        print('\nGuess ', i + 1, ': ', end = '')
                        Guess = list(str(int(input())))
                        if(len(Guess) != 3):
                            print('\nThe number entered is not a 3 digit number.')
                        else:
                            break
                    Clue = []
                    if(Guess == Num):
                        print('\nYou got it!\n')
                        break
                    for j in range(3):
                        if(Num[j] == Guess[j]):
                            Clue.append('Fermi')
                        elif(Guess[j] in Num):
                            Clue.append('Pico')
                        elif(j==2 and len(Clue) == 0):
                            Clue.append('Bagels')
                    shuffle(Clue)
                    print(Clue)
                    if(i == 6):
                        print('You ran out of guess. The number was ', Num, '\n')

            case 2:
                print('\n1. You have to guess a 3 digit number within 7 tries'
                      '\n2. You will get -'
                      '\n\tPico - One digit is correct but in the wrong position.'
                      '\n\tFermi - One digit is correct and in the right position.'
                      '\n\tBagels - No digit is correct.'
                      '\n3. Example -\n\tGuess 1: 123 \n\tPico'
                      '\n\tGuess 2: 456 \n\tBagels'
                      '\n\tGuess 3: 178 \n\tPico Pico'
                      '\n\tGuess 4: 791 \n\tFermi Fermi'
                      '\n\tGuess 5: 701 \n\tYou got it!\n')

            case 3:
                return '\nThanks for playing!'

            case _:
                print('\nInvalid choice')

print(Bagels())
