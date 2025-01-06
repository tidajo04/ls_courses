##########imports & constants#################################################
import random

VALID_CHOICES = {
                    "rock": ['rock', 'r', 'rck', 'rk', 'rc'],
                    "paper": ['paper', 'p', 'pa', 'pap', 'pape', 'pp', 'ppr', 
                              'papr', 'pper'],
                    "scissors": ['scissors', 'sc', 'sci', 'scis', 'sciss', 
                                'scissor', 'scssrs', 'scissr'],
                    "lizard": ['lizard', 'l', 'li', 'liz', 'lizz', 'lzr', 
                               'lzrd', 'lzard', 'z', 'zz', 'zrd', 'd'],
                    "spock": ['spock', 'sp', 'spo', 'spck', 'pock', 'spc', 
                              'spk']
}


#####Functions################################################################
user_score = 0      #variables used in a few functions below for game tracking
computer_score = 0      #tracks intra-game score
user_game_tally = 0
computer_game_tally =0  #tracks game wins

def prompt(message):
    print(f"==> {message}")

def welcome_message():
    print(' '.rjust(79, '*'))
    prompt('''Welcome to RPSLS_2.0, the world's most exhilerating,
    text-based, game of luck. The rules are simple, When prompted,
    chose a weapon: Rock, Paper, Scissors, Lizard, or Spock.

        -Rock beats Scissors and Lizard.
        -Paper beats Rock and Spock.
        -Scissors beat Paper and Lizard.
        -Lizard beats Paper and Spock.
        -Spock beats Rock and Scissors.

    Can you beat RPSLS_2.0 in this game of wits? Best of 5 takes the gold!

    Let's Begin.
           ''')
    print(' '.rjust(79, '*'))

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}.\n")

    global user_score
    global computer_score

    if ((player == "rock" and computer in ("scissors", "lizard")) or
        (player == "scissors" and computer in ("paper", "lizard")) or
        (player == "lizard" and computer in ("spock", "paper")) or
        (player == "spock" and computer in ("scissors", "rock"))):
        prompt("You get a point!")
        user_score += 1
    elif (player == computer):
        prompt("It's a tie! No points.")
    else:
        prompt("Computer gets a point!")
        computer_score += 1

def display_score():

    global user_game_tally
    global computer_game_tally

    print(f'<the score is player: {user_score}, computer: {computer_score}>\n')
    if user_score == 3:
        user_game_tally += 1
        prompt("You win! Congratulations!")
    if computer_score == 3:
        computer_game_tally += 1
        prompt("You lose! Better luck next time!")

def run_game():
    while user_score < 3 and computer_score < 3:
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
    #There must be a better way. Trying to stick with the idea of using a
    # Dictionary, but then I had to go through all this to make it readable
    # and be able to output a key from the user input item... had to use
    # GPT for help again... still havent entiely wrapped my head around this
    # and would need to look back to be able to do this again from memory.
    # is there a module that can usily look up keys associated within a list
    # of values in a dict?

        computer_choice = random.choice(list(VALID_CHOICES.keys()))
    #I guess .random wont select from a grouping of keys without turning
    #it into a list first? had to GPT troubleshoot here too.
        display_winner(choice, computer_choice)

        display_score()

#### Start Program ###########################################################
welcome_message()

while True:
    run_game() #made game loop separate from play_again options

    if user_game_tally == computer_game_tally:
        prompt(f"""You and the computer are tied {user_game_tally}
    to {computer_game_tally}! You can't quit on a draw,
    can you?

    Do you want to play again (y/n)?""")
        answer = input().casefold()

    if user_game_tally > computer_game_tally:
        prompt(f"""You're beating the computer {user_game_tally}
    to {computer_game_tally}! Won't you give us a chance to catch up?

    Do you want to play again (y/n)?""")
        answer = input().casefold()

    if user_game_tally < computer_game_tally:
        prompt(f"""You're down {user_game_tally}
    to {computer_game_tally}! You wouldn't want to quit now, would you?

    Do you want to play again (y/n)?""")
        answer = input().casefold()

    if answer.startswith('n'):
        prompt(f"""The final score is you: {user_game_tally},
    computer: {computer_game_tally}.
    
    GGs. Thank you for playing! Until next time!""")
        break
    elif answer.startswith('y'):
        prompt("Great, Let's run it back!\n")
        print(' '.rjust(79, '*'))
        user_score = 0
        computer_score = 0
        continue
    else:
        prompt("That's not a valid answer. Please try again (y/n)")
#####End Program##############################################################