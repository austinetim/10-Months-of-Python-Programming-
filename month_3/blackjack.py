###################### Black Jack ################
import random
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #Pick a random card
    card = random.choice(cards)
    return card


# Deal the user and computer 2 cards each using deal_card()



def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""


    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.add(1)
    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"  Your cards: {user_cards}, Current score: {user_score}")
print(f"  Computer's first cards: {computer_cards[0]}")
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to get another code, type 'n' to pass: ")
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else: 
        is_game_over = True
