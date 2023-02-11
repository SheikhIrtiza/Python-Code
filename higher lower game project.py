from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)
  
def format_data(account):
    """Format the account data into printable format."""
    name = account["name"]  #name of social media account like fb insta etc.
    description = account["description"]  #account description
    country = account["country"]
  #print(f'{name}:{account["follower_count"]}')#  
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_followers > b_followers:
       return guess == "a"
    else:
       return guess == "b"
    
# Display art
def game():
  print(logo)
  score = 0
  game_should_continue = True
# Generate a random account from the game data.
  account_a = get_random_account()  
  account_b = get_random_account()

#Make the game repeatable.
  while game_should_continue:

    #Making the account at position B become the next account posotion at A
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print("Compare A: {format_data(account_a)}.")
    print(vs)
    print("Against B: {format_data(account_b)}.")  #fxn call

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Clear the screen between rounds.
    clear()
    print(logo)

# Give user feedback on their guess
#Score keeeping.
    if is_correct:
      score += 1  #score incremented by 1
      print(f"You're right!!!  Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}.")

game()
'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B -  calligraphy_by_imsheikhirtiza(1k). Instagram has more 
followers, so choice A is correct. However, the subsequent comparison should be between calligraphy_by_imsheikhirtiza (the new A) and someone else. The reason is 
that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there
for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps
going up over the course of the game. Hope that makes sense :-)

'''
