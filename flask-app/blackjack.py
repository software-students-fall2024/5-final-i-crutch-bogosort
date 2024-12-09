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

def play_game():
    while True:
        #shuffle deck and initialize hands
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        #deal two cards to the player and the dealer
        player_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())

        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

        #reveal dealer cards
        show_some(player_hand, dealer_hand)

        playing = True
        while playing:
            #PLAYER ACTION: [HIT] / [STAND]
            choice = ''
            while choice.lower() not in ['h', 's']:
                choice = input("\nWould you like to Hit or Stand? (h/s): ")

            if choice.lower() == 'h':
                take_hit(deck, player_hand)
                if player_hand.value > 21:
                    show_all(player_hand, dealer_hand)
                    player_busts()
                    playing = False
            else:
                print("Player stands. Dealer's turn.\n")
                playing = False

        #if player did not bust, play dealer's hand
        if player_hand.value <= 21:
            show_all(player_hand, dealer_hand)
            while dealer_hand.value < 17:
                print("Dealer hits.")
                take_hit(deck, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts()
            elif dealer_hand.value > player_hand.value:
                dealer_wins()
            elif dealer_hand.value < player_hand.value:
                player_wins()
            else:
                push()

        new_game = ''
        while new_game.lower() not in ['y', 'n']:
            new_game = input("\nWould you like to play another hand? (y/n): ")
        if new_game.lower() == 'n':
            print("The session has ended.")
            break

if __name__ == "__main__":
    play_game()