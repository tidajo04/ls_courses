'''
1. Initialize deck
2. deal cards to player and dealer
3. player turn: hit or stay
    a. Ask player to hit or stay
    b. If stay, stop asking
    c. otherwise, go to a.
    repeat until bust or stay

4. if player busts, dealer wins
5. dealer turn: hit or stay
    - repeat until total => 17
6. if dealer busts, player wins.
7. compare cards and declare winner.
'''
############################# imports ########################################
import random

import json
with open('messages_21.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

import os

############################# CONSTANTS ######################################
SUITS = '♠♥♦♣'
CARDS = [' A', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7',
          ' 8', ' 9', '10', ' J', ' Q', ' K']
CARD_VALUES = {
    ' A': 11,
    ' 2': 2,
    ' 3': 3,
    ' 4': 4, 
    ' 5': 5, 
    ' 6': 6, 
    ' 7': 7,
    ' 8': 8,
    ' 9': 9,
    '10': 10,
    ' J': 10,
    ' Q': 10,
    ' K': 10
}

############################# Functions ######################################

def prompt(message):
    print(f'==> {message}')

def validate_binary_answers(option1, option2):
    #used to check user inputs, safegaurd from None entries or unexpected
    while True:
        answer = input().casefold()
        if not answer or answer[0] not in f'{option1}{option2}'.casefold():
            prompt(
                f"I'm sorry, I didn't understand your answer. "
                f"Please enter {option1} or {option2}"
            )
            continue
        return answer[0]
def delimiter():
    print('-----------------------------------------------------------------')

def full_card(hand):
    card_lines = []
    for card, suit in hand:
        c = f"{card:>2}"
        card_lines.append([
            f'|{c}‾‾‾|',
            f'|  {suit}  |',
            f'|___{c:>2}|',
        ])

    output_lines = []
    for i in range(3):
        line = '  '.join(card[i] for card in card_lines)
        output_lines.append(line)

    return '\n'.join(output_lines)


def display_intro():
    delimiter()
    prompt(
        f'Welcome to Twenty-One. Try to get as close to 21 as you can '
        f'without busting.'
        )
    delimiter()

def initialize_deck(deck):
    deck.extend([[card, suit] for suit in SUITS for card in CARDS])
    return deck

def shuffle(deck):
    random.shuffle(deck)

def deal_hands(player_hand, dealer_hand, deck):
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

def deal_card(deck):
    return deck.pop(0)

def total(hand):
    '''
    sums the value of the hand 
    and checks for ace adjustments (1 or 11)
    '''
    hand_value = 0

    for card in hand:
        hand_value += CARD_VALUES[card[0]]

    aces = [card[0] for card in hand].count('A')

    while hand_value > 21 and aces:
        hand_value -= 10
        aces -= 1

    return hand_value

def display_player_hand(player_hand):
    return full_card(player_hand)

def display_dealer_hand_hidden(dealer_hand):
    return full_card([['?', '?'], dealer_hand[1]])

def busted(hand):
    if total(hand) > 21:
        return True
    return False

def player_turn(player_hand, dealer_hand, deck):
    prompt(
        f'The dealer is showing\n{display_dealer_hand_hidden(dealer_hand)}')
    while True:
        prompt(
               f'Your hand is\n{display_player_hand(player_hand)}:\n '
               f'for a total of {total(player_hand)}'
            )
        if total(player_hand) == 21:
            prompt(" 21 Nice! let's see if the dealer can push")
            break
        elif busted(player_hand):
            prompt(f'{total(player_hand)} You\'ve busted!')
            break
        else:
            prompt("Hit (h) or Stay (s)? ")
            response = validate_binary_answers('h', 's')
            if response == 's':
                prompt(
                    f'You chose to Stay. '
                    f'You\'ve got a {total(player_hand)}'
                )
                break
            else:
                prompt(f"You chose to hit. Your next card is {deck[0]}")
                player_hand.append(deal_card(deck))

def dealer_turn(hand, deck):
    prompt(
        f"The dealer reveals its hidden card and is now showing\n"
        f"{full_card(hand)}:\n for a total of {total(hand)}"
    )
    while True:
        if total(hand) in range(17, 22):
            break
        elif busted(hand):
            prompt(f'a {total(hand)}: The dealer Busts!')
            break
        else:
            prompt(f'dealer hits: its next card is\n{full_card([deck[0]])}')
            hand.append(deal_card(deck))
            prompt(f'The dealer\'s at {total(hand)}')

def score_check(player_hand, dealer_hand):
    if total(player_hand) == total(dealer_hand):
        prompt("it's a push (a tie)!")
    elif total(player_hand) > total(dealer_hand):
        prompt(
            f'Your {total(player_hand)} beats the dealer\'s '
            f'{total(dealer_hand)}. You win!'
        )
    else:
        prompt(
            f'The dealer\'s {total(dealer_hand)} beats Your '
            f'{total(player_hand)}. You lose!'
        )
def play_again():
    prompt("should I deal another round? (y/n)")
    again_answer = validate_binary_answers('y', 'n')
    if again_answer != 'y':
        prompt('ggs then, Goodbye!')
        return False
    return True


def run_twenty_one():
    display_intro()
    while True:
        while True:
            deck = []
            player_hand = []
            dealer_hand = []
            initialize_deck(deck)

            shuffle(deck)

            prompt("dealing cards...")

            deal_hands(player_hand, dealer_hand, deck)

            player_turn(player_hand, dealer_hand, deck)
            if busted(player_hand):
                prompt("You Lose!")
                break

            dealer_turn(dealer_hand, deck)
            if busted(dealer_hand):
                prompt("You Win!")
                break

            score_check(player_hand, dealer_hand)
            break

        if not play_again():
            break


############################ Run Program #####################################
run_twenty_one()
