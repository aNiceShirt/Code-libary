import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

def score(hand):
    score = 0
    aces = 0
    for card in hand:
        score += card
        if card == 11:
            aces += 1
        if score > 21 and aces > 0:
            score -= 10
            aces -= 1
    return score

def print_hand(hand_owner,hand):
    print(f"{hand_owner} hand: {hand}, Total: {score(hand)}")


def blackjack():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the blackjack table")
    ### Start of game ###
    player_hand = []
    computer_hand = []
    lost = False
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    computer_hand.append(draw_card())
    computer_hand.append(draw_card())
    print(f"Dealer hand: [{computer_hand[0]}, X]")
    print_hand("Player",player_hand)

    while lost == False:
        if score(player_hand) > 21:
            lost = True
            print("You lost")
        if lost != True:
            draw = input("Draw a card? y/n: ")
            if draw == "y":
                    player_hand.append(draw_card())
                    print_hand("Player",player_hand)
            if draw == "n":
                print("You stand")
                print_hand("Player",player_hand)
                break

    while score(computer_hand) < 17:
        computer_hand.append(draw_card())

    if score(computer_hand) > 21 and score(player_hand) < 22:
        print_hand("Dealer",computer_hand)
        print("You won")

    elif score(computer_hand) < score(player_hand) and score(player_hand) < 22:
        print_hand("Dealer",computer_hand)
        print("You won")

    elif score(computer_hand) > score(player_hand) and score(player_hand) < 22:
        print_hand("Dealer",computer_hand)
        print("You lost")

    elif score(computer_hand) == score(player_hand) and score(player_hand) < 22:
        print("It's a draw")

    if input("Play again? (y/n)") == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()
    else:
        print("Goodbye")

blackjack()