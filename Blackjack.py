# Here's my favorite game: blackjack! 
# http://www.codeskulptor.org/#user45_55nfzdQcox_30.py
# Codeskulptor is only compatible with Google Chrome.

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome_result = ""
outcome_next_move = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        cards_string = "Hand contains "
        for card in self.cards:
            cards_string += str(card) +" "
        return cards_string 
    
    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        self.points = 0 
        numberOfAce = 0
        for card in self.cards: 
            self.points += VALUES[str(card)[1]] 
            if str(card)[1] == "A":
                numberOfAce += 1
        if (numberOfAce != 0 ) and (self.points + 10 <= 21):
            self.points += 10
        return self.points 
    
    def draw(self, canvas, pos):
        for card in self.cards:           
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(str(card)[1]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(str(card)[0]))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            pos[0] = pos[0] + CARD_SIZE[0] + 20
        
# define deck class 
class Deck:
    def __init__(self):
        self.one_deck = []
        for letter in SUITS:
            for number in RANKS:
                one_card = letter + number
                self.one_deck.append(one_card)

    def shuffle(self):
        random.shuffle(self.one_deck)
        
    def deal_card(self):
        number_of_cards = len(self.one_deck)
        item_drawn = random.randrange(0,number_of_cards)
        self.drawn_card = self.one_deck.pop(item_drawn)
        return self.drawn_card
    
    def __str__(self):
        deck_string = "Deck contains "
        for card in self.one_deck:
            deck_string += str(card) +" "
        return deck_string 

#define event handlers for buttons
def deal():
    global outcome_result, outcome_next_move, in_play, game_deck, dealer_hand, player_hand, score
    
    if in_play == True:
        score -= 1
    
    # create message and start in_play
    in_play = True 
    
    # create deck
    game_deck = Deck()
    game_deck.shuffle()
    
    # deal four cards, two for player and two for dealer
    c1 = game_deck.deal_card()
    c2 = game_deck.deal_card()
    c3 = game_deck.deal_card()
    c4 = game_deck.deal_card()

    # add cards to dealer's and player's hand
    dealer_hand = Hand()
    dealer_hand.add_card(c1)
    dealer_hand.add_card(c2)

    player_hand = Hand()
    player_hand.add_card(c3)
    player_hand.add_card(c4)
    
    outcome_result = ""
    outcome_next_move = "Hit or stand?"
                        
def hit():
    global player_hand, game_deck, outcome_result, outcome_next_move, in_play, score

    # if the hand is in play, hit the player
    if in_play == True:
        
        card = game_deck.deal_card()
        player_hand.add_card(card)
        player_score = player_hand.get_value()
        # if busted, assign a message to outcome, update in_play and score
        if player_score > 21: 
            outcome_result = "You went bust and lose."
            outcome_next_move = "New deal?" 
            in_play = False
            score -= 1
    else: 
        outcome_next_move = "You cannot hit."
           
def stand():
    global player_hand, dealer_hand, game_deck, outcome_next_move,outcome_result, in_play, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    if in_play == False:
        outcome_next_move = "You cannot stand. You have busted." 
    else:
        in_play = False
        # assign a message to outcome, update in_play and score
        while dealer_hand.get_value() < 17:
            card = game_deck.deal_card()
            dealer_hand.add_card(card)
            
        if dealer_hand.get_value()>21:
            outcome_result = "Dealer has busted. You won!"
            outcome_next_move = "New deal?"
            score +=1
            
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome_result = "You lost."
            outcome_next_move = "New deal?"
            score -=1
        
        elif dealer_hand.get_value() < player_hand.get_value():
            outcome_result = "You won!"
            outcome_next_move = "New deal?"
            score +=1

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below    
    
    canvas.draw_text("Blackjack", [100,60],60, "Aqua","monospace")
    canvas.draw_text("Score: " + str(score), [100,110],30, "Black","monospace")
    canvas.draw_text(outcome_result, [220,160],30, "black","monospace")
    canvas.draw_text("Dealer", [50,160],30,"black","monospace")
    canvas.draw_text(outcome_next_move,[220,380],30,"black","monospace")
    canvas.draw_text("Player", [50,380],30,"black","monospace")


    player_hand.draw(canvas,[80,400])
    dealer_hand.draw(canvas,[80,200])
    
    if in_play == True:
        back_card_loc = (CARD_BACK_SIZE[0]+CARD_BACK_CENTER[0],CARD_BACK_CENTER[1] )

        canvas.draw_image(card_back, back_card_loc, CARD_BACK_SIZE, 
                          [80 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
# remember to review the gradic rubric
