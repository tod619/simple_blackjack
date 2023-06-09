# Simple Blackjack
# A simple game of blackjack to explore the game logic
# 30/05/2023
import random
import os


def compare_score(score1, score2):
    if score1 == score2:
        return "Draw!"
    elif score2 == 0:
        return "Computer wins BlackJack Baby!!"
    elif score1 == 0:
        return "Player wins BlackJack Baby!!"
    elif score1 > 21:
        return "Player went bust! Computer wins!!"
    elif score2 > 21:
        return "Computer went bust! Player wins!!"
    elif score1 > score2:
        return "You Win"
    else:
        return "You have lost"


def deal_card():
    """ Return a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # simple card deck
    card = random.choice(cards)  # shuffle deck
    return card  # return random card


# my_card = deal_card()
# print(my_card)


# print(user_cards)
# print(computer_cards)

# Create Function to calculate the score


def calculate_score(card_hand):
    """ A function to calculate the value of a hand of cards """
    if 11 in card_hand and 10 in card_hand and len(card_hand) == 2:
        # if sum(card_hand) == 21 and len(card_hand) == 2:
        return 0

    if 11 in card_hand and sum(card_hand) > 21:
        card_hand.remove(11)
        card_hand.append(21)

    return sum(card_hand)


# print(calculate_score(user_cards))
# print(calculate_score(computer_cards))
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # deal the computer + user 2 cards each
    for round in range(2):
        # new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Player Cards: {user_cards} Player Score: {user_score}")
    print(f"Computers First Card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_hit = input("Type y to hit or n to stand: ").lower()
        if user_hit == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Player Cards: {user_cards} Player Score: {user_score}")
        print(f"Computers First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_hit = input("Type y to hit or n to stand: ").lower()
            if user_hit == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Player hand: {user_cards} Player Score: {user_score}")
    print(f"Computer hand: {computer_cards} Computer Score: {computer_score}")
    result = compare_score(user_score, computer_score)
    print(result)


while input("Do you want to play Blackjack? y or n: ") == 'y':
    os.system("CLS")
    play_game()

input("\n\nPress enter to exit ")
