import random
from art import logo
from replit import clear
end_game = False

def deal_card(cards):
      """Returns a random card from the deck"""
      random_card = random.choice(cards)
      return random_card

def calculate_score(list_of_cards):
      """Takes list of cards and returns the score calculated from the cards"""
      if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
      if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
      return sum(list_of_cards)
  
def compare(user_score, computer_score):
      if user_score == computer_score:
        return "It's a draw!"
      elif computer_score == 0:
        return "Opponent has Blackjack! You loose."
      elif user_score == 0:
        return "You have a Blackjack! You win!"
      elif user_score > 21:
        return "You went over 21, you loose."
      elif computer_score > 21:
        return "Opponent went over 21, you win!"
      elif user_score > computer_score:
        return "You reached higher score, you win!"
      elif user_score < computer_score:
        return "Computer has higher score. You loose" 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  end_game = False
  print(logo)
  tab = '\t'
  user_cards = []
  computers_cards = []
  for _ in range(2):
    user_cards.append(deal_card(cards))
    computers_cards.append(deal_card(cards))
  
  while not end_game:
    user_score = calculate_score(user_cards)
    computers_score = calculate_score(computers_cards)
    print(f"{tab}Your cards: {user_cards}, current score: {user_score}")
    print(f"{tab}Computer's first card: {computers_cards[0]}")
  
    if computers_score == 0 or user_score == 0 or user_score > 21:
      end_game = True
    else:
      get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if get_another_card == "y":
        user_cards.append(deal_card(cards)) 
      else:
        end_game = True
        
  while computers_score != 0 and computers_score < 17:
    computers_cards.append(deal_card(cards))
    computers_score = calculate_score(computers_cards)
    
  print(f"{tab}Your final hand is {user_cards}, your final score is {user_score}")
  print(f"{tab}Computers final hand is {computers_cards}, computer's final score is {computers_score}")
  print(compare(user_score, computers_score))
  
while input("Do you want to play a game of Backjack? 'y' or 'n'? ") == "y":
  clear()
  blackjack() 
