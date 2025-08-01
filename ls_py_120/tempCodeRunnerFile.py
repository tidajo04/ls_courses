import random
import os

def clear_screen():
    os.system('clear')

class Card:
    SUITS = ['♠', '♥', '♦', '♣']
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        top = "┌─────┐"
        middle_top = f"│{self.rank:<2}   │"    # Left-aligned rank
        middle_mid = f"│  {self.suit}  │"     # Centered suit
        middle_bot = f"│   {self.rank:>2}│"   # Right-aligned rank
        bottom = "└─────┘"
        return "\n".join([top, middle_top, middle_mid, middle_bot, bottom])
        

class Hand:
    CARD_VALUES = {
        **{rank:rank for rank in Card.RANKS if isinstance(rank, int)}, 
        **{rank:10 for rank in ['J', 'Q', 'K']},
        **{'A':11}
    }
    def __init__(self):
        self.cards_in_hand = []

    def add_hand(self, cards):
        for card in cards:
            self.add_card(card)
    
    def add_card(self, card):
        self.cards_in_hand.append(card)

    def score(self):
        hand_total = sum(Hand.CARD_VALUES[card.rank] for card in self.cards_in_hand)
        num_aces = sum(1 for card in self.cards_in_hand if card.rank == "A")

        while hand_total > 21 and num_aces > 0:
            hand_total -= 10
            num_aces -= 1

        return hand_total
    
    def is_busted(self):
        return self.score() > 21

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)

    def draw_hand(self):
        return [self.draw_card() for _ in range(2)]

    def draw_card(self):
        return self.cards.pop()


class Dealer:
    def __init__(self):
        self.hand = Hand()
        self.hide_second_card = True

    def hide_card(self):
        pass

    def reveal_card(self):
        self.hide_second_card = False

class Player:
    def __init__(self, starting_chips):
        self.hand = Hand()
        self.chips = starting_chips
        self.pot = 0
        
    def display_chips(self):
        print(self.chips)

    def bet(self):
        while True:
            try:
                bet = int(input("Place a bet: "))
                if 0 < bet <= self.chips:
                    self.chips -= bet
                    self.pot = bet
                    return True
                else:
                    print("That is not a valid bet.")
            except ValueError:
                print("Please enter a whole number.")

    def resolve_bet(self, result):
        if result == "Blackjack":
            bonus = max(round(self.pot * .25), 1)
            self.chips += self.pot * 2 + bonus
            print(f"You win your {self.pot} bet AND earned {bonus} bonus chip(s)!")
        elif result == "Player":
            self.chips += self.pot * 2
            print(f"You win. You made {self.pot} chip(s)!")
        elif result == "Push":
            self.chips += self.pot
            print(f"It's a push. You get your {self.pot} chip(s) back.")
        elif result == "Dealer":
            print(f"You lose. You lost {self.pot} chip(s).")
        self.pot = 0

class Table:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def display_hand(self, cards, hide_second=False):
        card_lines = []
        for i, card in enumerate(cards):
            if i == 1 and hide_second:
                hidden = ["┌─────┐", "│ ??? │", "│ ??? │", "│ ??? │", "└─────┘"]
                card_lines.append(hidden)
            else:
                card_lines.append(str(card).split('\n'))

        for i in range(len(card_lines[0])):
            print(' '.join(card[i] for card in card_lines))

    def display_state(self):
        clear_screen()
        print(f'You have {self.player.chips} chips left')
        print("Dealer's hand:")
        self.display_hand(self.dealer.hand.cards_in_hand, self.dealer.hide_second_card)

        if not self.dealer.hide_second_card:
            print(f"Dealer's score: {self.dealer.hand.score()}")

        print("Player's hand:")
        self.display_hand(self.player.hand.cards_in_hand)
        print(f"Player's score: {self.player.hand.score()}")

    def display_chips(self):
        print(f"You have {self.player.chips} chips")

class Hello_Goodbye_Messages:
    def __init__(self, player):
        self.player = player

    @property
    def thanks(self):
        return "Thanks for playing!"

    @property
    def broke(self):
        return "Oh, sorry. You're broke. I'm gunna have to ask you to leave."

    @property
    def nice_day(self):
        return "Have a nice day!"

    @property
    def final_count(self):
        return f"Your final chip count is {self.player.chips}. Come again soon!"
    
    @property
    def greeting(self):
        return "Hello, Welcome to Twenty-One"
    
class TwentyOneGame:
    PLAYER_CHIP_START = 10
    def __init__(self):
        self.deck = Deck()
        self.player = Player(self.PLAYER_CHIP_START)
        self.dealer = Dealer()
        self.table = Table(self.player, self.dealer)
        self.message = Hello_Goodbye_Messages(self.player)

    def display_starting_chips(self, num):
        print(f"You've been aloted {num} chips to start this game. Good Luck!")

    def reset_deck_if_low(self):
        if len(self.deck.cards) <26:
            self.deck = Deck()
            self.deck.shuffle()
            print("Deck is low, re-shuffleing")

    def play(self):
        
        print(self.message.greeting)
        while True:
            self.reset_deck_if_low()
            self.table.display_chips()
            self.player.bet()
            self.deal_starting_hands()

            blackjack_result = self.handle_blackjack()
            if blackjack_result is True:
                continue
            elif blackjack_result is False:
                break

            self.table.display_state()
            self.player_turn()
            self.dealer_turn()
            self.table.display_state()
            self.player.resolve_bet(self.is_winner())

            if self.player.chips == 0:
                print(self.message.broke)
                print(self.message.nice_day)
                break
            if not self.play_another_hand():
                print(self.message.final_count)
                break

    def player_turn(self):
        while self.player.hand.score() < 21:
            move = input("hit or stay: ").strip().casefold()
            while True:
                if move.startswith('h'):
                    self.deal_card_for(self.player.hand) 
                    self.table.display_state()
                    break
                elif move.casefold().startswith('s'):
                    return
                else:
                    print("that's not a valid move")
    
    def play_another_hand(self):
        while True:
            response = input("Would you like to play another hand? (y/n) ")
            clear_screen()
            if response.startswith('y'):
                return True
            elif response.startswith('n'):
                return False
            else: 
                print("I'm sorry that is not a valid choice")

    def handle_blackjack(self):
        player_score = self.player.hand.score()
        dealer_score = self.dealer.hand.score()
        player_is_bj = player_score == 21 and len(self.player.hand.cards_in_hand) == 2
        dealer_is_bj = dealer_score == 21 and len(self.dealer.hand.cards_in_hand) == 2

        if player_is_bj or dealer_is_bj:
            self.dealer.reveal_card()
            self.table.display_state()

            if player_is_bj and dealer_is_bj:
                print("Blackjack tie! Both you and the dealer have blackjack.")
                self.player.resolve_bet("Push")  # still a push, no bonus
            elif dealer_is_bj:
                print("Dealer has blackjack.")
                self.player.resolve_bet("Dealer")
            else:
                print("Blackjack!")
                self.player.resolve_bet("Blackjack")

            if self.player.chips == 0:
                print("You're broke. Game over.")
                return False

            if not self.play_another_hand():
                print(f"Your final chip count is {self.player.chips}. Come again soon!")
                return False

            return True

        return None

    def dealer_turn(self):
        self.dealer.reveal_card()
        self.table.display_state()
        while self.dealer.hand.score() <= 16 and not self.player.hand.is_busted():
            self.deal_card_for(self.dealer.hand)
        
    def deal_starting_hands(self):
        self.player.hand.cards_in_hand = []
        self.dealer.hand.cards_in_hand = []
        self.player.hand.add_hand(self.deck.draw_hand())
        self.dealer.hand.add_hand(self.deck.draw_hand())
        self.dealer.hide_second_card = True
    
    def deal_card_for(self, hand):
        hand.add_card(self.deck.draw_card())
        
    def is_winner(self):
        if self.player.hand.score() == 21 and len(self.player.hand.cards_in_hand) == 2:
            return "Blackjack"
        if self.player.hand.is_busted():
            return "Dealer"
        if self.dealer.hand.is_busted():
            return "Player"
        if self.player.hand.score() == self.dealer.hand.score():
            return "Push"
        if self.player.hand.score() > self.dealer.hand.score():
            return "Player"
        
        return "Dealer"
    
to = TwentyOneGame()
to.play()


