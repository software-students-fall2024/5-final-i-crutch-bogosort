import pytest
from blackjack import Deck, Hand, Card, ranks, values, take_hit, show_some

def test_deck_initialization():
    deck = Deck()
    assert len(deck.all_cards) == 52

    rank_count = {}
    for card in deck.all_cards:
        rank_count[card.rank] = rank_count.get(card.rank, 0) + 1
    for rank in ranks:
        assert rank_count.get(rank, 0) == 4

def test_deck_deal_one():
    deck = Deck()
    card = deck.deal_one()
    assert len(deck.all_cards) == 51
    assert isinstance(card, Card)

def test_card_str():
    card = Card('A')
    assert str(card) == 'A'

def test_hand_add_card_no_ace():
    hand = Hand()
    hand.add_card(Card('5'))  
    hand.add_card(Card('K')) 
    assert hand.value == 15

def test_hand_add_card_with_ace():
    hand = Hand()
    hand.add_card(Card('A')) 
    hand.add_card(Card('9')) 
    assert hand.value == 20

    hand.add_card(Card('A'))
    assert hand.value == 21

@pytest.mark.parametrize("rank,expected_value", [
    ('2', 2), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11)
])
def test_card_values(rank, expected_value):
    assert values[rank] == expected_value

def test_take_hit():
    deck = Deck()
    hand = Hand()
    initial_deck_size = len(deck.all_cards)
    take_hit(deck, hand)
    assert len(hand.cards) == 1
    assert len(deck.all_cards) == initial_deck_size - 1

def test_show_some(capsys):
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(Card('5'))
    player_hand.add_card(Card('K'))
    dealer_hand.add_card(Card('Q'))
    dealer_hand.add_card(Card('8'))

    result = show_some(player_hand, dealer_hand)
    expected = (
        "Dealers Hand:@(X 8)@Player Hand:@5, K (Value: 15)"
    )

    assert result == expected, f"Expected {expected}, but got {result}"