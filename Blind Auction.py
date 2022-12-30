from replit import clear
all_bidders = {}
stop_bidding = False
while not stop_bidding:
  name = input("What is your name? ")
  bid = input("What's your bid? $")
  all_bidders[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  clear()
  if other_bidders == 'no':
    stop_bidding = True
    for highest_bidder in all_bidders:
      highest_bidder = max(all_bidders, key = all_bidders.get)
      highest_bid = all_bidders[highest_bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
