############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
from replit import clear
import random

cards_dict = {
  1:1,
  2:2,
  3:3,
  4:4,
  5:5,
  6:6,
  7:7,
  8:8,
  9:9,
  10:10,
  11:"Jack",
  12:"Queen",
  13:"King",
  14:"Ace",
}
cards_score_dict = {
  1:1,
  2:2,
  3:3,
  4:4,
  5:5,
  6:6,
  7:7,
  8:8,
  9:9,
  10:10,
  11:10,
  12:10,
  13:10,
  14:11,
}

def draw_card():
  card1 = random.randint(1, 14)
  return card1

def show_hand(hand1, comp_bool):
  if comp_bool:
    comp_hand_show = ""
    for card in range(0,len(hand1)-1):
      comp_hand_show += (str(cards_dict[hand1[card]])+" ")
    return comp_hand_show
  else:
    play_hand_show = ""
    for card in range(0,len(hand1)):
      play_hand_show += (str(cards_dict[hand1[card]])+" ")
    return play_hand_show

def get_score(hand1):
  score1 = 0
  contains_ace = False
  for card in hand1:
    if card == 14:
      contains_ace = True
    score1 += cards_score_dict[card]
  #redo score if they bust an have an ace
  if contains_ace and score1 > 21:
    score1 = 0
    for card in hand1:
      if card == 14:
        score1 += 1
      else:
        score1 += cards_score_dict[card]
  return score1

def main():
  print(art.logo)
  continue1 = True

  #generate both hands and score variables
  player_hand = [draw_card(), draw_card()]
  computer_hand = [1, draw_card()]

  player_score = get_score(player_hand)
  computer_score = get_score(computer_hand)

  #show both hands
  print(f"Your hand is {show_hand(player_hand, False)}")
  print(f"Your score is {get_score(player_hand)}")
  print(f"The dealer showing card is {show_hand(computer_hand, True)}\n")

  continue1 = True
  while continue1:
    draw_choice = input("Do you want to draw another card, y for yes, n for no: ")
    print("\n")
    #if computer score <13 must draw_card
    while computer_score < 13:
      print(f"Dealer score is less than 13, so dealer must draw a card")
      computer_hand.append(draw_card())
      computer_score = get_score(computer_hand)
      print(f"The dealer showing cards are {show_hand(computer_hand, True)}\n")

    if draw_choice == "y":
      player_hand.append(draw_card())
      print(f"\nYour hand is now {show_hand(player_hand, False)}")
      player_score = get_score(player_hand)
      print(f"Your score is now {player_score}")
      print(f"The dealer showing card is {show_hand(computer_hand, True)}\n")
      
      
    if draw_choice == "n" or computer_score > 21 or player_score > 21:
      continue1 = False
    
  print(f"\nTime to reveal dealer hand: {show_hand(computer_hand, False)} which gives them a score of: {computer_score}\n")
  
  if player_score > 21:
    print(f"Since your score of {player_score} is over 21, you lose!")
  elif computer_score > 21:
    print(f"Since dealer score is over 21, you win!")
  elif player_score > computer_score:
    print(f"Since your score of {player_score} is higher than the dealer, you win!")
  else:
    print(f"Since your score of {player_score} is lower or tied with dealer, you lose!")

main()


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

