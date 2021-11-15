import art
import random
import game_data

def pick_people():
  return random.randint(0,49)

def check_prev(persona, list_prev):
  for item in list_prev:
    if item == persona:
      return True
  return False

def same_people(persona, personb):
  if persona == personb:
    return True
  else:
    return False

def main():
  print(art.logo_higher)
  print("Welcome to higher or lower.\nYou will have to guess which person has more followers on social media.\n")

  score1 = 0
  continue1 = True
  prev_persons= []
  person1= pick_people()
  person2= pick_people()
  
  while continue1:
    #initial pick
    person1= person2
    person2= pick_people()
    #add these to list so we dont pick again for b/#2
    prev_persons.append(person1)
    prev_persons.append(person2)
    #if they were a previous pick pick again, or the same
    while check_prev(person2, prev_persons) or same_people(person1, person2):
      person2= pick_people()

    #print pick names and description with versus logo between
    print(f"{game_data.data[person1]['name']} a {game_data.data[person1]['description']} from {game_data.data[person1]['country']}")
    print(art.vs)
    print(f"{game_data.data[person2]['name']} a {game_data.data[person2]['description']} from {game_data.data[person2]['country']}")    

    guess1 = input("Who has more followers? Type 'A' or 'B' ").lower()

    #bring in follower counts from dict in game_data
    followers1 = game_data.data[person1]['follower_count'] 
    followers2 = game_data.data[person2]['follower_count']

    if guess1 == 'a' and followers1 > followers2:
      print(f"\nYou got it right {game_data.data[person1]['name']} has more followers.")
      score1 += 1
      print(f"Your score is now {score1}.\n\n\n")
    elif guess1 == 'b' and followers2 > followers1:
      print(f"\nYou got it right {game_data.data[person2]['name']} has more followers.")
      score1 += 1
      print(f"Your score is now {score1}.\n\n\n")
    else:
      print(f"\nYou got it wrong.")      
      print(f"Your final score is {score1}.\n")
      continue1 = False

main()
