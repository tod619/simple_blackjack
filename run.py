# Simple Blackjack
# A simple game of blackjack to explore the game logic
# 30/05/2023
import random

user_cards = []
computer_cards = []


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
