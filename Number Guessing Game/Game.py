import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  difficulty = input("Choose a difficulty level. Type 'easy' or 'hard' ")
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  elif difficulty == 'hard':
    return HARD_LEVEL_TURNS
  else:
    print("Invalid input")

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.\nGuess again.")
    return turns - 1
  elif guess < answer:
    print ("Too low. \nGuess again")
    return turns - 1
  else:
    print(f"You got it! The answer in {answer}")
    
def game():
  print(logo)
  print("Welcome to the Number Guessing Game! \nI'm thinking of the number between 1 and 100.")
  answer = random.randint(1, 100)
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses, you loose.")
      return
game()
