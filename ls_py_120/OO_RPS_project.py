import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class RPSGame:
    ROUNDS = 2
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self.human_score = 0
        self.computer_score = 0

    def _display_welcome_message(self):
        print(f'Welcome to Rock Paper Scissors! first to {RPSGame.ROUNDS} wins!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
                (human_move == 'paper' and computer_move == 'rock') or
                (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                (computer_move == 'paper' and human_move == 'rock') or
                (computer_move == 'scissors' and human_move == 'paper'))

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            self.human_score += 1
            print('You win!')
        elif self._computer_wins():
            self.computer_score += 1
            print('Computer wins!')
        else:
            print("It's a tie")

    def _display_score(self):
        if self.human_score < RPSGame.ROUNDS and self.computer_score < RPSGame.ROUNDS:
            print(f'The score is: Player, {self.human_score} - Computer, {self.computer_score}')
        else:
            winner = "Player" if self.human_score > self.computer_score else "Computer"
            print(f'The final tally is: Player, {self.human_score} - Computer, {self.computer_score}\n'
                  f'the grand champion is {winner}')

    def _reset_score(self):
        self.human_score = 0
        self.computer_score = 0

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            self._reset_score()
            while self.human_score < RPSGame.ROUNDS and self.computer_score < RPSGame.ROUNDS:
                self._human.choose()
                self._computer.choose()
                self._display_winner()
                self._display_score()
            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()
