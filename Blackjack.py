from random import choice

DealtCards = []
Cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
Values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Group = ['♣', '♦', '♥', '♠']
PSum, DSum = 0, 0
PBust, DBust = False, False

def GetCard(is_Player):
    global PSum, DSum
    Number = choice(Cards)
    Index = Cards.index(Number)
    Card = Number + choice(Group)
    while(Card in DealtCards):
        Number = choice(Cards)
        Index = Cards.index(Number)
        Card = Number + choice(Group)
    if(is_Player):
        if(Index == 0 and PSum <= 10):
            PSum += 11
        elif(Index == 0):
            PSum += 1
        else:
            PSum += Values[Index]
    else:
        if(Index == 0 and DSum <= 10):
            DSum += 11
        elif(Index == 0):
            DSum += 1
        else:
            DSum += Values[Index]
    DealtCards.append(Card)
    return Card

def Blackjack():
    global PBust, DBust, PSum, DSum, DealtCards
    Balance = 4000
    Bet = 0
    while(True):
        PlayerCards, DealerCards, DealtCards = [], [], []
        PSum, DSum = 0, 0
        PBust, DBust = False, False
        print('\n1.Start game \n2.Rules \n3.Exit')
        ch = float(input('\nEnter your choice: '))
        match ch:
            case 1:
                print('Balance = ', Balance)
                Bet = int(input('\nEnter your bet: '))
                while (Bet > Balance):
                    if(Bet <= Balance):
                        break
                    elif(Bet > Balance):
                        print('\nInsufficient balance')
                        print('Current Balance =', Balance, 'c')
                        Bet = int(input('\nEnter your bet: '))
                    else:
                        print('\nInvalid input')
                print('\nProceeding with', Bet, 'c as your bet.')
                DC = GetCard(False)
                PlayerCards.extend((GetCard(True), GetCard(True)))
                DealerCards.extend((GetCard(False), DC))

                print("\nDealer's cards are: ['Not Revealed', '{}']".format(DC))
                print('Your Cards are:', PlayerCards, 'Value =', PSum)

                while(PSum < 21):
                    print('\n(H)it / (S)tand')
                    c = input('\nEnter Your Choice: ')
                    if(c == 'h' or c == 'H'):
                        PlayerCards.append(GetCard(True))
                        print('Your Cards:', PlayerCards, 'Value = ', PSum)
                    elif(c == 's' or c == 'S'):
                        print('Your Cards:', PlayerCards, 'Value = ', PSum)
                        print('\nYour turn has ended.')
                        break
                    else:
                        print('Invalid Choice')
                print('Your turn has ended.')  
                
                if(PSum > 21):
                    PBust = True                        
                while(DSum < 17 and PBust != True):
                    DealerCards.append(GetCard(False))
                    if(DSum > 21):
                        DBust = True

                print('\nYour Cards:', PlayerCards, 'Value = ', PSum)
                print('Dealer\'s Cards:', DealerCards, 'Value = ', DSum)

                if(PBust == True):
                    print('You are busted!')
                    Result = 'Lose'
                elif(DBust == True):
                    print('Dealer was busted!')
                    Result = 'Win'
                elif(PSum > DSum):
                    Result = 'Win'
                elif(PSum == DSum and PSum <= 21):
                    Result = 'Tie'
                else:
                    Result = 'Lose'
                    
                if(Result == 'Win'):
                    print('\nYou Won! You have gained', Bet*1.5 - Bet, 'c.')
                    Balance += Bet*0.5
                elif(Result == 'Tie'):
                    print('\nIt was a tie! You gained nothing.')
                else:
                    print('\nDealer Wins! You lost', Bet, 'c.')
                    Balance -= Bet
                print('Remaining Balance = ', Balance)
                if(Balance == 0):
                    return '\nYou are out of money. Ending game...'
                    
                print('\n1.Continue game \n2.Exit')
                ch = int(input('\nEnter your choice: '))
                while(ch!=2 or ch!=1):
                    if (ch==2):
                        return '\nThanks for playing!'
                    elif (ch == 1):
                        break
                    else:
                        print('\nInvalid Choice!')
                        ch = int(input('\nEnter your choice: '))
                        
            case 2:
                print('\n1. Goal: Get a hand value as close to 21 as possible without going over (busting). You start with 4000c Balance.'
                      '\n2. Card Values:'
                      '\n\ti) Number cards (2-10) are worth their face value.'
                      '\n\tii) Face cards (Jack, Queen, King) are worth 10.'
                      '\n\tiii) Ace is worth 1 or 11, whichever is more advantageous.'
                      '\n3. Gameplay:'
                      '\n\ti) Dealing: Both player and the dealer, receives two cards. Player cards are face up and dealer has one card face u[ and one card face down.'
                      '\n\tii) Player\'s Turn:'
                      '\n\t\t> Hit: Take another card to increase your hand value.'
                      '\n\t\t> Stand: Keep your current hand and end your turn.'
                      '\n\tiii) Dealer\'s Turn: The dealer reveals their face-down card and must hit until their hand value is at least 17. They stand on 17 or higher.'
                      '\n4. Winning and Losing:'
                      '\n\ti) Player Wins: If your hand is closer to 21 than the dealer\'s without busting, or if the dealer busts.'
                      '\n\tii) Dealer Wins: If the dealer\'s hand is closer to 21 without busting, or if you bust.'
                      '\n\tiii) Tie: If your hand value is the same as the dealer\'s, it\'s a tie (no one wins or loses)'
                      '\n5. Blackjack: Getting a hand of 21 with your first two cards (an Ace and a 10-value card) is called Blackjack.'
                      '\n6. Payout: Wins are paid out at 1:1 ratio, except for player Blackjack, which is paid out at 3:2 ratio.\n')
            
            case 3:
                return '\nThanks for playing!'
            
            case _:
                print('\nInvalid choice')

print(Blackjack())