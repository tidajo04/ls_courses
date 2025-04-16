#TIC TAC TOE
'''
1. Display the initial empty 3x3 board.
    if doing this in all text, going to need to lookup formating 
        with "------" for horz
        and "|" for vertical

2. Ask the user to mark a square.
    by selecting based on a grid ? a1 a2 a3, b1 b2 b3, c1 c2 c3
    or by selecting a number 1-9. after giving instructions.

3. Computer marks a square.
4. Display the updated board state.
    augment the area in the board with an 'X: or "O" based on the player.
    and the computer.
5. If it's a winning board, display the winner.
6. If the board is full, display tie.
7. If neither player won and the board is not full, go to #2
8. Play again?
9. If yes, go to #1
    but switch the starting player.
10. Goodbye!
'''
############################### Imports ######################################

import json
with open('messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)
import random
import os

############################### CONSTANTS ####################################

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
MATCH_WIN = 3
WINNING_LINES = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
FIRST_TO_PLAY = ''
############################### FUNCTIONS ####################################
def prompt(message):
    print(f"==> {message}")

def display_board(board):
    '''wipes terminal and displays the current state of the board'''
    os.system('clear')

    prompt(f'you are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('') #changed numbers to match num pad placement
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |     ')
    print('')

def initialize_board():
    '''creates a new empty board (for new games)'''
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    '''creates a reference list to check for playable positions'''
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    '''for user to input turn selections'''
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        user_input = input().strip()
        if not user_input:
            continue

        try: #added this to fix error raised by a misclicked non-input
            square = int(user_input)
            if square in empty_squares(board):
                break
        except ValueError:
            pass

        prompt(MESSAGES['invalid_choice'])

    board[square] = HUMAN_MARKER

def join_or(numbers, delimiter=',', conjunction='or'):
    '''pretties up the available choices'''
    lst = [str(i) for i in numbers]

    if len(lst) == 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return f'{lst[0]} {conjunction} {lst[1]}'

    return f"{delimiter} ".join(lst[:-1]) + \
           f'{delimiter} {conjunction} {lst[-1]}'

def find_at_risk_square(board):
    '''Computer AI: checks for win/loss conditions'''
    for line in WINNING_LINES: #checks if win is possible first
        c_count = 0
        empty_spot = None

        for num in line:
            if board[num] == COMPUTER_MARKER:
                c_count += 1
            elif board[num] != HUMAN_MARKER:
                empty_spot = num

        if c_count == 2 and empty_spot is not None:
            return empty_spot

    for line in WINNING_LINES: #checks if loss is possible second
        h_count = 0
        empty_spot = None

        for num in line:
            if board[num] == HUMAN_MARKER:
                h_count += 1
            elif board[num] != COMPUTER_MARKER:
                empty_spot = num

        if h_count == 2 and empty_spot is not None:
            return empty_spot

    return None

def computer_chooses_square(board):
    '''determines computer's turn'''
    if len(empty_squares(board)) == 0:
        return

    if find_at_risk_square(board):         #returns none if no win/loss at risk
        board[find_at_risk_square(board)] = COMPUTER_MARKER
    elif board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER
    else:                                  #goes random if no other risks
        square = random.choice(empty_squares(board))
        board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        if (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won(board):
    return bool(detect_winner(board))

def validate_binary_answers(option1, option2):
    '''used to check user inputs, safegaurd from None entries or unexpected'''
    while True:
        answer = input().casefold()
        if not answer or answer[0] not in f'{option1}{option2}'.casefold():
            prompt(f'{MESSAGES['invalid_bin_answer']} {option1} or {option2}')
            continue
        return answer[0]

def choose_difficulty():
    '''prompts message to user to allow difficulty change'''
    prompt(MESSAGES['difficulty_select'])
    return validate_binary_answers('e','h')

def play_tic_tac_toe():
    '''base gameplay loop'''
    prompt(MESSAGES["welcome"])
    prompt(MESSAGES["input_rules"])

    print('')
    difficulty = choose_difficulty() #sets initial difficulty
    print('')

    prompt(f"Good luck, first to {MATCH_WIN} wins it all!")

    matches = 0

    while True:

        if matches > 0: #avoids re-asking on the first match
            prompt(MESSAGES["difficulty_change"])
            answer = validate_binary_answers('y','n')
            if answer == 'y':
                difficulty = choose_difficulty()
        score = {"Player": 0, "Computer": 0}
        while score["Player"] < MATCH_WIN and score["Computer"] < MATCH_WIN:
            prompt(f'Score: Player - {score["Player"]}, Computer - {score["Computer"]}')
            prompt(MESSAGES["enter_ready"])
            input()
            board = initialize_board()

            if difficulty == 'e':
                while True:
                    display_board(board)

                    player_chooses_square(board)

                    if someone_won(board) or board_full(board):
                        break

                    computer_chooses_square(board)

                    if someone_won(board) or board_full(board):
                        break
            else:
                while True:
                    computer_chooses_square(board)
                    display_board(board)

                    if someone_won(board) or board_full(board):
                        break

                    player_chooses_square(board)

                    if someone_won(board) or board_full(board):
                        break

            display_board(board)

            if someone_won(board):
                prompt(f'{detect_winner(board)} won!')
                score[detect_winner(board)] += 1

            else:
                prompt(MESSAGES["tie"])

        matches += 1


        prompt(f"""
    Great Match! The score is:
    Player - {score['Player']}, Computer - {score['Computer']}
    {detect_winner(board)} is the champion!!!

    Would you like to play another match? (y or n)"
    """
            )
        score["Player"] = 0
        score["Computer"] = 0

        answer = validate_binary_answers('y','n')

        os.system('clear')

        if answer[0] != 'y':
            prompt(MESSAGES["ggs"])
            break

############################## PROGRAM #######################################
play_tic_tac_toe()
