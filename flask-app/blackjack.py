import random

ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11 
}

class Card:
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return f"{self.rank}"

class Deck:
    def __init__(self):
        #initialize deck with 4 of each rank to 
        #simulate a standard 52-card deck 
        self.all_cards = [Card(rank) for rank in ranks for _ in range(4)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0  #total value of the hand
        self.aces = 0   #number of aces in the hand

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        #if total value >21 and there are aces, 
        #adjust the ace value from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return ', '.join(str(card) for card in self.cards) + f" (Value: {self.value})"

def take_hit(deck, hand):
    card = deck.deal_one()
    hand.add_card(card)
    result = f"Dealt card: {card}@Hand now: {hand}"
    return result

def show_some(player, dealer):
    result = "Dealers Hand:@(X "
    if dealer.cards:
        result+= dealer.cards[1].__str__() + ")"
    result += f"@Player Hand:@{player.__str__()}"
    return result

def show_all(player, dealer):
    result = f"Dealers Hand: {dealer}@Player Hand: {player}"
    return result

def player_busts():
    return "You busts! Deaer wins."

def player_wins():
    return "You win!"

def dealer_busts():
    return "Dealer busts! You win."

def dealer_wins():
    return "Dealer wins!"

def push():
    return "It's a tie! Push."