import random
from art import logo, vs
from game_data import data
from replit import clear

def select_celebrity():
  """Returns random celebrity from database."""
  celebrity = random.choice(data)
  return celebrity

def format_data(celebrity):
  """Takes the celebrity's data and returns the printable format."""
  celebrity_name = celebrity["name"]
  celebrity_descr = celebrity["description"]
  celebrity_country = celebrity["country"]
  return f"{celebrity_name}, a {celebrity_descr}, from {celebrity_country}"

def compare_followers(celebrity1_followers, celebrity2_followers, answer):
  """Takes the users answer and follower counts and returns if they guesse right."""
  if answer == "a":
    return celebrity1_followers > celebrity2_followers
  if answer == "b":
    return celebrity2_followers > celebrity1_followers


print(logo)
score = 0
continue_game = True
celebrity2 = select_celebrity()

while continue_game:
  celebrity1 = celebrity2
  celebrity2 = select_celebrity()
  
  while celebrity1 == celebrity2:
    celebrity2 = select_celebrity()
    
  print(f"Compare A: {format_data(celebrity1)}.")
  print(vs)
  print(f"Against B: {format_data(celebrity2)}.")

  answer = (input("Who has more followers? Type 'A' or 'B': ")).lower()
  celebrity1_followers = celebrity1["follower_count"]
  celebrity2_followers = celebrity2["follower_count"]
  compare_followers(celebrity1_followers, celebrity2_followers, answer)
  
  clear()
  print(logo)
  if compare_followers(celebrity1_followers, celebrity2_followers, answer) == True:
    score += 1
    print(f"You're right! Your score is {score}")
  else:
    continue_game = False
    print(f"Sorry, you're wrong. Final score is {score}")
