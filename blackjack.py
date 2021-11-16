"""
MODULE DOCSTRING
"""
from random import shuffle
from itertools import product
from IPython.display import clear_output

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine','Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':[1,11]}
all_cards = product(suits,ranks)

class Card:
    """
    Creates the cards for the game with rank and suit, respectively from
    ranks and suits tuples; value is attributed based on the values
    dictionary and used for comparison.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """
    Creates a deck of 52 cards using the Card class.
    """
    def __init__(self):
        self.cards = [Card(suit, rank) for suit, rank in all_cards]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        shuffle(self.cards)

class Player:
    """
    DOCSTRING
    """
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0
        self.balance = 0

    def get_card(self):
        """
        Adds the last card from the deck to the player. The value of the
        card is added to the player score used to evaluate the winner.
        """
        self.score += deck.cards[-1].value
        self.cards.append(deck.cards.pop(-1))
        
    def place_bet(self):
        """
        Places the bet using the player's money. 
        """
        self.balance -= self.bet
        
    def win(self):
        """
        Adds the total of the jackpot to player's balance.
        """
        self.balance += jackpot


gambler = Player('gambler')
dealer = Player('dealer')

deck = Deck()
deck.shuffle()

def show_table():
    """
    Shows the cards drawn by the players.
    """
    print('GAMBLER')
    for card in gambler.cards:      
        print(card)
    print(gambler.score)

    print('\nDEALER')
    for card in dealer.cards[1:]:
        print(card)
    print(dealer.score)

def hit_stand():
    jackpot = 0
    playing = True
    stance = ''
    
    gambler.balance = int(input('How much money do you have to play? '))
    dealer.balance = gambler.balance * 10
    gambler.bet = int(input('Place your bet: '))
    dealer.bet = gambler.bet
    gambler.place_bet()
    dealer.place_bet()
    
    jackpot += (gambler.bet+dealer.bet)
    
    while len(gambler.cards) < 2:
        gambler.get_card()
        dealer.get_card()
    while len(dealer.cards) < 2:
        gambler.get_card()
        dealer.get_card()
    print('\nGAMBLER')
    for card in gambler.cards:      
        print(card)

    print('\nDEALER')
    for card in dealer.cards[1:]:
        print(card)

    while playing:
        while stance not in ('H','S', 'h', 's'):
            
            stance = input("Hit or stand? (H/S) ").lower()
            if stance == 's':
                playing = False
                clear_output()
                while dealer.score <= 17:
                    dealer.get_card()
                    
                print('\nGAMBLER')
                for card in gambler.cards:      
                    print(card)
                print(gambler.score)
                
                print('\nDEALER')
                for card in dealer.cards:
                    print(card)
                print(dealer.score)
                    
                if dealer.score > gambler.score:
                    if dealer.score <= 21:
                        print('\nThe house wins!')
                        dealer.win()
                    else:
                        print('\nYou win!')
                        gambler.win()
                elif dealer.score < gambler.score:
                    if gambler.score <= 21:
                        print('\nYou win!')
                        gambler.win()
                    else:
                        print('\nBust! The house wins!')
                        dealer.win()
                else:
                    print('\nPush!')
                break
                

            else:
                clear_output()
                gambler.get_card()
                
                print('\nGAMBLER')
                for card in gambler.cards:      
                    print(card)

                print('\nDEALER')
                for card in dealer.cards[1:]:
                    print(card)
                      
                if gambler.score > 21:
                    print('\nBust! You lose!')
                    playing = False
                    break
                stance = ''
    print('Here!')           
    jackpot = 0
                


