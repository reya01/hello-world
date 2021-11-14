#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

def make_a_guess(attempts_left, correct_number):
  print(f"\nYou have {attempts_left} attempts left to guess the number.")
  guess1 = int(input("Make a guess: "))
  if guess1 == correct_number:
    return True
  else:
    print("Sorry that wasn't the number")
    if guess1 > correct_number:
      print("Your guess was too high.\n")
    else:
      print("Your guess was too low.\n")
    return False

def main():
  print(art.welcome)
  print("\n\nWelcome to the Number Guessing Game!!!")
  print("I am think of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  the_number = random.randint(1,100)
  num_attempts = 10
  if difficulty == "hard":
    num_attempts -= 5

  while num_attempts > 0:
    if make_a_guess(num_attempts, the_number):
      print(f"Congrats you guessed the correct number, {the_number}")
      print(art.win)
      num_attempts = 0
    else:
      num_attempts -= 1
      if num_attempts == 0:
        print("\nYou run out of guesses, you lose.\n")


main()
