#### Imports & Constants #####################################################
import random

VALID_CHOICES = {
    "rock"    : ['rock', 'r', 'rck', 'rk', 'rc', 'ro', 'roc'],
    "paper"   : ['paper', 'p', 'pa', 'pap', 'pape', 'pp', 'ppr', 'papr', 
                 'pper'],
    "scissors": ['scissors', 'sc', 'sci', 'scis', 'sciss', 'scissor', 
                 'scssrs', 'scissr'],
    "lizard"  : ['lizard', 'l', 'li', 'liz', 'lizz', 'lzr', 'lzrd', 'lzard', 
                 'z', 'zz', 'zrd', 'd'],
    "spock"   : ['spock', 'sp', 'spo', 'spck', 'pock', 'spc', 'spk']
}

WINNING_CHOICES = {
        "rock"    : ["scissors", "lizard"],
        "paper"   : ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard"  : ["spock", "paper"],
        "spock"   : ["scissors", "rock"]
    }

WIN_NUM = 3

#### Functions ###############################################################
#formats print function for pretty display
def prompt(message):
    print(f"==> {message}")

#prints greeter
def welcome_message():
    print(' '.rjust(79, '*'))
    prompt(
    '''Welcome to RPSLS_2.0, the world's most exhilerating, text-based game
    of luck. The rules are simple, When prompted, chose a  weapon: Rock, 
    Paper, Scissors, Lizard, or Spock.
           
        - Rock beats Scissors and Lizard.
        - Paper beats Rock and Spock.
        - Scissors beat Paper and Lizard.
        - Lizard beats Paper and Spock.
        - Spock beats Rock and Scissors.

    Can you beat the computer in this game of wits? 
    Best of 5 takes the gold!

    Let's Begin."
    ''')
    print(' '.rjust(79, '*'))

#Tests win, displays result, and adds to score
def display_winner(player, computer, user_score, computer_score):
    prompt(f"You chose {player}, computer chose {computer}.\n")

    if player == computer:
        prompt("It's a tie! No points.")
    elif computer in WINNING_CHOICES[player]:
        prompt("You get a point!")
        user_score += 1
    else:
        prompt("Computer gets a point!")
        computer_score += 1

    return user_score, computer_score

#tests win condition, displays game over message, & tallies total games count
def display_score(user_score, computer_score, user_tally, computer_tally):

    print(f'<Score is player: {user_score}, computer: {computer_score}>\n')
    if user_score == WIN_NUM:
        user_tally += 1
        print('XXXXXXXXXXXXXXXXXXXX GAME OVER XXXXXXXXXXXXXXXXXXXX')
        prompt("You win! Congratulations!\n")
    if computer_score == WIN_NUM:
        computer_tally += 1
        print('XXXXXXXXXXXXXXXXXXXX GAME OVER XXXXXXXXXXXXXXXXXXXX')
        prompt("You lose! Better luck next time!\n")

    return user_tally, computer_tally

#nested functions into gameplay loop & validates user input = valid choice
def run_game(user_score, computer_score, user_tally, computer_tally):
    while user_score < WIN_NUM and computer_score < WIN_NUM:
        prompt(f'Choose one: {", ".join(VALID_CHOICES.keys())}')
        choice_input = input()

        choice = None
        for key, aliases in VALID_CHOICES.items():
            if choice_input.casefold() in [alias.casefold()
                                           for alias in aliases]:
                choice = key
                break

        while not choice:
            prompt("That's not a valid choice. Please try again.")
            choice_input = input()
            for key, aliases in VALID_CHOICES.items():
                if choice_input.casefold() in [alias.casefold()
                                               for alias in aliases]:
                    choice = key
                    break

        computer_choice = random.choice(list(VALID_CHOICES.keys()))

        user_score, computer_score = display_winner(choice, computer_choice,
                                                user_score, computer_score)

        user_tally, computer_tally = display_score(user_score,
                                                computer_score, user_tally,
                                                computer_tally)

    return user_score, computer_score, user_tally, computer_tally

#custom game over messgae for replay prompt
def game_state_replay_prompt(user_tally, computer_tally):
    if user_tally == computer_tally:
        prompt(
        f"""You're tied {user_tally} to {computer_tally}!
    You can't quit on a draw, can you?
    """)

    if user_tally > computer_tally:
        prompt(
        f"""You're winning {user_tally} to {computer_tally}!
    Won't you give us a chance to catch up?
    """)

    if user_tally < computer_tally:
        prompt(
        f"""You're down {user_tally} to {computer_tally}!
    You wouldn't want to quit now, would you?
    """)

#main game function (uses all others)
def play_rpsls():
    welcome_message()

    user_tally = 0
    computer_tally = 0

    while True:
        user_score = 0
        computer_score = 0

        user_score, computer_score, user_tally, computer_tally =\
                            run_game(user_score, computer_score,
                                     user_tally, computer_tally)

        game_state_replay_prompt(user_tally, computer_tally)
        while True:
            prompt("Do you want to play again? (y/n)")
            answer = input().casefold()

            if answer.startswith('n'):
                prompt(
            f"""The final score is:
    you: {user_tally}, computer: {computer_tally}.
            
    GGs. Thank you for playing! Until next time!""")
                return
            if answer.startswith('y'):
                prompt("Great, Let's run it back!\n")
                print(' '.rjust(79, '*'))
                user_score = 0
                computer_score = 0
                break

            prompt("That's not a valid answer. Please try again (y/n)")
#### Start Program ###########################################################
play_rpsls()