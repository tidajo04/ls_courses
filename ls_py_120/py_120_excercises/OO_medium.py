# PP1 Circular Buffer
# class CircularBuffer:
#     def __init__(self, size):
#         self.size = size
#         self.container = []

#     def put(self, num):
#         if len(self.container) == self.size:
#             self.container.pop(0)         
#         self.container.append(num)   
        
#     def get(self):

#         if self.container:
#             return self.container.pop(0) #remove and return oldest item
#         return None

# buffer = CircularBuffer(3)

# print(buffer.get() is None)          # True

# buffer.put(1)
# buffer.put(2)
# print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True

# PP2 & 3
# import random
# import math
# class GuessingGame:
#     def __init__(self, low, high):
#         self.low = low
#         self.high = high
#         self.NUM_RANGE = range(self.low, self.high + 1)
        
    
#     def play(self):
#         answer = random.choice(self.NUM_RANGE)
#         tries = int(math.log2(self.high - self.low + 1)) + 1
#         valid_guess = f"{self.NUM_RANGE[0]} and {self.NUM_RANGE[-1]}"
        
#         while tries > 0:
#             if tries == 1:
#                 print(f"You have {tries} guess remaining.")
#             else:
#                 print(f"You have {tries} guesses remaining.")

#             while True:
#                 guess_input = input(f"Enter a number between {valid_guess}: ")
#                 try:
#                     guess = int(guess_input)
#                     if guess in self.NUM_RANGE:
#                         break  # valid input, move on
#                     else:
#                         print(f"Invalid guess. ", end="")
#                 except ValueError:
#                     print(f"Invalid guess. ", end="")
                 
#             if guess == answer:
#                 print("That's the number!")
#                 print("You won!")
#                 return None
#             elif guess > answer:
#                 print("Your guess is too high.")
#             elif guess < answer:
#                 print("Your guess is too low.")
#             tries -= 1
#             print('')
            

#         print(f"You have no more guesses. The number was {answer}. You lost!")
#         return None

# game = GuessingGame(200, 900)
# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!

#PP4 

class Card:
    CARD_RANKS = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9,
                   'Jack':10, 'Queen':11, 'King': 12, 'Ace': 13}
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __lt__(self, other):
        return self.CARD_RANKS[self.rank] < other.CARD_RANKS[other.rank]
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# cards = [Card(2, 'Hearts'),
#          Card(10, 'Diamonds'),
#          Card('Ace', 'Clubs')]
# print(min(cards) == Card(2, 'Hearts'))             # True
# print(max(cards) == Card('Ace', 'Clubs'))          # True
# print(str(min(cards)) == "2 of Hearts")            # True
# print(str(max(cards)) == "Ace of Clubs")           # True

# cards = [Card(5, 'Hearts')]
# print(min(cards) == Card(5, 'Hearts'))             # True
# print(max(cards) == Card(5, 'Hearts'))             # True
# print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

# cards = [Card(4, 'Hearts'),
#          Card(4, 'Diamonds'),
#          Card(10, 'Clubs')]
# print(min(cards).rank == 4)                        # True
# print(max(cards) == Card(10, 'Clubs'))             # True
# print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

# cards = [Card(7, 'Diamonds'),
#          Card('Jack', 'Diamonds'),
#          Card('Jack', 'Spades')]
# print(min(cards) == Card(7, 'Diamonds'))           # True
# print(max(cards).rank == 'Jack')                   # True
# print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

# cards = [Card(8, 'Diamonds'),
#          Card(8, 'Clubs'),
#          Card(8, 'Spades')]
# print(min(cards).rank == 8)                        # True
# print(max(cards).rank == 8)                        # True

# PP5
import random
class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.deck = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
        random.shuffle(self.deck)
    
    def draw(self):
        if not self.deck:
            self.__init__()
        return self.deck.pop()


# deck = Deck()
# drawn = []
# for _ in range(52):
#     drawn.append(deck.draw())

# count_rank_5 = sum([1 for card in drawn if card.rank == 5])
# count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

# print(count_rank_5 == 4)      # True
# print(count_hearts == 13)     # True

# drawn2 = []
# for _ in range(52):
#     drawn2.append(deck.draw())

# print(drawn != drawn2)        # True (Almost always).

# PP6

# Include Card and Deck classes from the last two exercises.
