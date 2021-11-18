"""
This is blackjack game meant to be played by a player against the
computer. At its current state, it's a single player game and uses
the most basic rules of blackjack; i.e., there's no split, double
down etc.
"""
from random import shuffle
from itertools import product
from IPython.display import clear_output

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine','Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}
all_cards = list(product(suits,ranks))

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
        self.bet = 0

    def get_card(self):
        """
        Adds the last card from the deck to the player. The value of the
        card is added to the player score.
        """
        self.score += deck.cards[-1].value
        self.cards.append(deck.cards.pop(-1))

    def place_bet(self):
        """
        Asks the player to place a bet. The ammount cannot be higher than
        the curent balance of the player.
        """
        while True:
            try:
                self.bet = int(input('Place your bet: '))
                if self.bet <= self.balance:
                    break
                #else
                clear_output()
                print (f'Your bet cannot exceed your balance (${self.balance}).')
            except ValueError:
                clear_output()
                print('Choose a valid number.')
        self.balance -= self.bet

def initial_deal():
    """
    Deals two cards for both the gambler and the dealer.
    Both cards of the gambler are revealed, but only the
    top one of the dealer.
    """
    clear_output()
    while len(gambler.cards) < 2:
        gambler.get_card()
        dealer.get_card()
    while len(dealer.cards) < 2:
        gambler.get_card()
        dealer.get_card()
    show_table()

def show_table():
    """
    Shows the cards drawn by both the dealer and the player. The
    first card drawn by the dealer remains hidden.
    """
    print('DEALER', dealer.cards[1], sep='\n')

    print('\nGAMBLER', *gambler.cards, sep='\n')
    print(gambler.score)

def show_table_end():
    """
    Shows the cards drawn by both the dealer and the player. The
    first card drawn by the dealer is shown. The score of both is
    also shown.
    """
    print('DEALER', *dealer.cards, sep='\n')
    print(dealer.score)

    print('\nGAMBLER', *gambler.cards, sep='\n')
    print(gambler.score)

def hit_stand():
    """
    Asks the gambler if he wishes to take another card
    (hit) or not (stand). If hits, he receives another
    card. If he stands, no more cards are dealt for him
    and the dealer must draw cards until he reachs a
    value of 17 or above.
    """
    stance = ''
    while stance not in ('h', 's'):
        stance = input("Hit or stand? (H/S) ").lower()
        if stance == 'h':
            clear_output()
            gambler.get_card()
            show_table()
            if gambler.score > 21:
                return 'h'
            stance = ''
        elif stance == 's':
            clear_output()
            while dealer.score <= 17:
                dealer.get_card()
    return stance

def result():
    """
    Compares the score of the gambler and the dealer for
    a winner or a tie (push). If the gambler gets 21 at
    the initial draw, he has a blackjack. If the player
    exceeds 21, it's a bust.
    """
    if gambler.score == dealer.score:
        match_result = 'push'
    elif gambler.score == 21:
        match_result = 'blackjack'
        gambler.balance += (gambler.bet+dealer.bet)
    elif gambler.score > 21:
        match_result = 'gambler_busts'
    elif dealer.score > 21:
        match_result = 'dealer_busts'
        gambler.balance += (gambler.bet+dealer.bet)
    elif gambler.score > dealer.score:
        match_result = 'gambler_wins'
        gambler.balance += (gambler.bet+dealer.bet)
    elif gambler.score < dealer.score:
        match_result = 'dealer_wins'
    return match_result

def winner():
    """
    Adds the respective ammount of money to players'
    balance based on the result of the round.
    """
    result()
    if result() == 'push':
        gambler.balance += gambler.bet
        dealer.balance += dealer.bet
        print("\nIt's a tie! Nobody wins and the bets are returned.")

    elif result() in ('blackjack', 'gambler_wins', 'dealer_busts'):
        gambler.balance += (gambler.bet+dealer.bet)
        print(f'\nThe gambler gets ${gambler.bet+dealer.bet}.')

    elif result() in ('gambler_busts', 'dealer_wins'):
        dealer.balance += (gambler.bet+dealer.bet)
        print(f'\nThe dealer gets ${gambler.bet+dealer.bet}.')
    gambler.bet = 0
    dealer.bet = 0
def ace_value():
    """
    Adjusts the value of ace. Aces are normally valued at 11. If the
    player score exceeds 21, it's reduced by 10 to 1 to avoid bust.
    This can only occur for one ace in the player's cards.
    """
    if gambler.score > 21:
        if 'Ace' in [card.rank for card in gambler.cards]:
            gambler.score -= 10
    if dealer.score > 21:
        if 'Ace' in [card.rank for card in dealer.cards]:
            dealer.score -= 10

def replay():
    """
    Clears the scores and the hands of the players.
    """
    gambler.cards = []
    dealer.cards = []
    gambler.score = 0
    dealer.score = 0

while True:
    gambler = Player('gambler')
    dealer = Player('dealer')

    gambler.balance = 10000
    dealer.balance = gambler.balance * 5

    print(f"You have ${gambler.balance} to play today!")

    playing = True

    while playing is True:
        deck = Deck()
        deck.shuffle()
        gambler.place_bet()
        dealer.bet = gambler.bet
        dealer.balance -= dealer.bet
        initial_deal()
        ace_value()
        if result() == 'blackjack':
            winner()
            playing = False
        while True:
            if hit_stand() == 's':
                ace_value()
                playing = False
                break
            ace_value()
            playing = False
            break

        clear_output()
        show_table_end()
        winner()

        if gambler.balance == 0:
            print('Too bad! You ran out of money!')
            break
        play_again = ''
        while play_again not in ('y', 'n'):
            play_again = input('Play again? (y/n) ').lower()
            clear_output()
        if play_again == 'y':
            replay()
            playing = True
        else:
            print(f'Your final balance is ${gambler.balance}')
    break
