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
user_score = 0      #variables used in a few functions below for game tracking
computer_score = 0      #tracks intra-game score
user_game_tally = 0
computer_game_tally = 0  #tracks game wins

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
def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}.\n")

    global user_score
    global computer_score

    if player == computer:
        prompt("It's a tie! No points.")
    elif computer in WINNING_CHOICES[player]:
        prompt("You get a point!")
        user_score += 1
    else:
        prompt("Computer gets a point!")
        computer_score += 1

#tests win condition, displays game over message, & tallies total games count
def display_score():

    global user_game_tally
    global computer_game_tally

    print(f'<The score is player: {user_score}, computer: {computer_score}>\n')
    if user_score == WIN_NUM:
        user_game_tally += 1
        print('XXXXXXXXXXXXXXXXXXXX GAME OVER XXXXXXXXXXXXXXXXXXXX')
        prompt("You win! Congratulations!\n")
    if computer_score == WIN_NUM:
        computer_game_tally += 1
        print('XXXXXXXXXXXXXXXXXXXX GAME OVER XXXXXXXXXXXXXXXXXXXX')
        prompt("You lose! Better luck next time!\n")

#nested functions into gameplay loop & validates user input = valid choice
def run_game():
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
    #^There must be a better way. Trying to stick with the idea of using a
    # Dictionary, but then I had to go through all this to make it readable
    # and be able to output a key from the user input item... had to use
    # GPT for help again... still havent entiely wrapped my head around this
    # and would need to look back to be able to do this again from memory.
    # is there a module that can easily look up keys associated within a list
    # of values in a dict?

        computer_choice = random.choice(list(VALID_CHOICES.keys()))
    #^I guess .random wont select from a grouping of keys without turning
    #it into a list first? had to GPT troubleshoot here too.
        display_winner(choice, computer_choice)

        display_score()

#custom game over messgae for replay prompt
def game_state_replay_prompt():
    if user_game_tally == computer_game_tally:
        prompt(
        f"""You're tied {user_game_tally} to {computer_game_tally}!
    You can't quit on a draw, can you?
    """)

    if user_game_tally > computer_game_tally:
        prompt(
        f"""You're winning {user_game_tally} to {computer_game_tally}!
    Won't you give us a chance to catch up?
    """)

    if user_game_tally < computer_game_tally:
        prompt(
        f"""You're down {user_game_tally} to {computer_game_tally}!
    You wouldn't want to quit now, would you?
    """)

#### Start Program ###########################################################
welcome_message()

while True:
    run_game() #made game loop separate from play_again options

    game_state_replay_prompt()

    prompt("Do you want to play again? (y/n)")
    answer = input().casefold()

    if answer.startswith('n'):
        prompt(
    f"""The final score is:
    you: {user_game_tally}, computer: {computer_game_tally}.
    
    GGs. Thank you for playing! Until next time!""")
        break
    if answer.startswith('y'):
        prompt("Great, Let's run it back!\n")
        print(' '.rjust(79, '*'))
        user_score = 0
        computer_score = 0
        continue
    else:
        prompt("That's not a valid answer. Please try again (y/n)")
#### End Program #############################################################