###################### Black Jack ################
import random
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #Pick a random card
    card = random.choice(cards)
    return card


# Deal the user and computer 2 cards each using deal_card()

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):

    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0


    return sum(cards)