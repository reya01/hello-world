
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
  card1 = random.randint(2, 14)#originally forgot there was not 1 card, lol
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

