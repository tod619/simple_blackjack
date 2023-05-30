# Simple Blackjack
# A simple game of blackjack to explore the game logic
# 30/05/2023
import random

user_cards = []
computer_cards = []


def deal_card():
    """ Return a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # simple card deck
    card = random.choice(cards)  # shuffle deck
    return card  # return random card


# my_card = deal_card()
# print(my_card)

# deal the computer + user 2 cards each
for round in range(2):
    # new_card = deal_card()
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

input("\n\nPress enter to exit ")
