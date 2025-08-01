import random

# class Game:
#     def __init__(self):
#         self.human_score = 0
#         self.computer_score = 0
#         self.human = Human('X')
#         self.computer = Computer('O')

#     def play(self):
#         while True:
#             self.board = Board()
#             self.display_greeting()
#             self.display_board()
#             self.play_turns()
#             self.display_board()

#             winner = self.get_winner()
#             self.display_winner(winner)
#             self.update_score(winner)
#             self.display_score()

#             if not self.play_again():
#                 print("Thanks for playing!")
#                 break

#     def display_greeting(self):
#         print('Ready to begin Tic Tac Toe. Player is "X", Computer is "O".')

#     def display_board(self):
#         print(self.board)

#     def play_turns(self):
#         current_player = self.human
#         while self.board.gamestate():
#             current_player.move(self.board)
#             self.display_board()
#             if not self.board.gamestate():
#                 break
#             current_player = self.human if current_player == self.computer else self.computer

#     def get_winner(self):
#         return self.board.winner()

#     def display_winner(self, winner):
#         if winner == 'Human':
#             print("You win!")
#         elif winner == 'Computer':
#             print("Computer wins!")
#         else:
#             print("It's a tie.")

#     def update_score(self, winner):
#         if winner == 'Human':
#             self.human_score += 1
#         elif winner == 'Computer':
#             self.computer_score += 1

#     def display_score(self):
#         print(f'Score - You: {self.human_score}, Computer: {self.computer_score}')

#     def play_again(self):
#         answer = input('Would you like to play again (y/n)? ')
#         return answer.lower().startswith('y')

# class Board:
#     def __init__(self):
#         self.spaces = {i: ' ' for i in range(1, 10)}

#     def __str__(self):
#         blank_line = '-'*5 + '|' + '-'*5 + '|' + '-'*5
#         return (
#             f'  {self.spaces[1]}  |  {self.spaces[2]}  |  {self.spaces[3]}\n'
#             f'{blank_line}\n'
#             f'  {self.spaces[4]}  |  {self.spaces[5]}  |  {self.spaces[6]}\n'
#             f'{blank_line}\n'
#             f'  {self.spaces[7]}  |  {self.spaces[8]}  |  {self.spaces[9]}\n'
#         )

#     def gamestate(self):
#         return self.winner() is None and any(space == ' ' for space in self.spaces.values())

#     def update_board(self, move, marker):
#         if self.spaces.get(move, 'X') == ' ':
#             self.spaces[move] = marker
#         else:
#             print("That square is taken. Try again.")
#             self.update_board(int(input("Enter a different number 1-9: ")), marker)

#     def winner(self):
#         WINNING_LINES = [
#             [1, 2, 3], [4, 5, 6], [7, 8, 9],
#             [1, 4, 7], [2, 5, 8], [3, 6, 9],
#             [1, 5, 9], [3, 5, 7]
#         ]
#         for line in WINNING_LINES:
#             values = [self.spaces[i] for i in line]
#             if values[0] != ' ' and all(val == values[0] for val in values):
#                 return 'Human' if values[0] == 'X' else 'Computer'
#         return None

# class Player:
#     def __init__(self, marker):
#         self.marker = marker

# class Human(Player):
#     def move(self, board):
#         while True:
#             try:
#                 move = int(input('Enter a number (1-9): '))
#                 if move in board.spaces and board.spaces[move] == ' ':
#                     board.update_board(move, self.marker)
#                     break
#                 else:
#                     print("Invalid move. Try again.")
#             except ValueError:
#                 print("Please enter a valid number.")

# class Computer(Player):
#     def move(self, board):
#         available_moves = [pos for pos, val in board.spaces.items() if val == ' ']
#         move = random.choice(available_moves)
#         print(f"Computer chooses: {move}")
#         board.update_board(move, self.marker)

# # Launch the game

# ttt = Game()
# ttt.play()
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = ' '
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.squares = {key: Square() for key in range(1,10)}

    def display_with_clear(self):
        clear_screen()
        print('\n')
        self.display()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |  {self.squares[5]}  |  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)
    


class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )
    MATCH_WIN = 3
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.score = {'Player': 0, "Computer": 0}
        self.first_player = self.human

    def play(self):
        self.display_welcome_message()
        current_player = self.first_player

        while True:
            self.board.reset()
            self.board.display()

            while True:
                self.player_moves(current_player)
                if self.is_game_over():
                    break

                self.board.display_with_clear()
                current_player = self.toggle_player(current_player)

            self.board.display_with_clear()
            
            self.update_score()
            self.display_score()
            input('Press any key to continue...')
            if self.score["Player"] == 3 or self.score["Computer"] == TTTGame.MATCH_WIN:
                clear_screen()
                self.display_score()
                self.display_results()
                if not self.play_again():
                    self.display_goodbye_message()
                    break

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human
    
    def player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def display_score(self):
        print(f"The score is Player: {self.score['Player']}, Computer: {self.score['Computer']}")

    def update_score(self):
        if self.is_winner(self.human):
            self.score["Player"] += 1
        if self.is_winner(self.computer):
            self.score["Computer"] += 1

    def play_again(self):
        
        while True:
            answer = input("would you like to play again? (y/n) ").strip().casefold()
            if answer.startswith('y'):
                print("hell yes! lets do this!")
                clear_screen()
                return True
            elif answer.startswith('n'):
                return False
            else:
                print("that's not a valid answer.")
                print()

    def display_welcome_message(self):
        clear_screen()
        print(f"Welcome to Tic Tac Toe! ... First to {TTTGame.MATCH_WIN} wins!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congradulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie gmae. How boring...")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def human_moves(self):
        valid_choices = self.board.unused_squares()
        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame._join_or(choices_list)
            prompt = f"Choose a square from ({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print('Sorry, that\'s not a valid choice.')
            print()

        self.board.mark_square_at(choice, self.human.marker)

    @staticmethod
    def _join_or(choice_list, delimeter=', ', conjunction='or'):
        
        if len(choice_list) == 1:
            return choice_list[0]
        if len(choice_list) == 2:
            return f'{choice_list[0]} {conjunction} {choice_list[1]}'
        
        return f'{delimeter.join(choice_list[:-1])} {conjunction} {choice_list[-1]}'
    
    def AI_best_square(self):
        valid_choices = self.board.unused_squares()
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            markers = [self.board.squares[key].marker for key in row]

            if markers.count(Square.COMPUTER_MARKER) == 2 and markers.count(Square.INITIAL_MARKER) == 1:
                for key in row:
                    if self.board.squares[key].marker == Square.INITIAL_MARKER:
                        return key
            if markers.count(Square.HUMAN_MARKER) == 2 and markers.count(Square.INITIAL_MARKER) == 1:
                for key in row:
                    if self.board.squares[key].marker == Square.INITIAL_MARKER:
                        return key
            if 5 in valid_choices:
                return 5
        return random.choice(valid_choices)
    
    def computer_moves(self):
        choice = self.AI_best_square()

        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row ) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or self.is_winner(self.computer))

game = TTTGame()
game.play()
