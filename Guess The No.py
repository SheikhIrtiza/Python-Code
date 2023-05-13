# importing modules
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10 #we can guess 10 times if we choose easy level of difficulty.
HARD_LEVEL_TURNS = 5  #we can guess 5 times  _____________________________________.
#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else: 
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
#    return easy levels if the dificulty is choosen easy
    return EASY_LEVEL_TURNS
  else:
    #   else hard levels if the difficulty is choosen hard
    return HARD_LEVEL_TURNS

def game():#new function
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 
 
  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
#   unless guess is not equal to answer loop will keep going
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong. Now we will try to reduce no. of attemots
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
#     condition if the guess is not answer then the guess again will be printed
    elif guess != answer:
      print("Guess again.")


game()#call function of def game():

