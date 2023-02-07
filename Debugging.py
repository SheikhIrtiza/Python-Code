############DEBUGGING#####################

# Describe Problem
#def my_function():
 # for i in range(1, 21):
  #  if i == 20:
   #   print("You got it")
#my_function()

# # Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)#prints the dice from index (0-5)that is dice:- 1,2,3,4,5,6
#print(dice_imgs[dice_num])

# # Play Computer
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:
 # print("You are a millenial.")
#elif year >= 1994:
 # print("You are a Gen Z.")

# # Fix the Errors
#age = int(input("How old are you?"))
#if age > 18:
 # print(f"You can drive at age {age}.")

# #Print is Your Friend
#pages = 0#pages start out at 0
#word_per_page = 0#words start out at 0
#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))
#total_words = pages * word_per_page#multiplication of total pages
#print(total_words)

# #Use a Debugger
#lists are mutable , we can update it
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2#here we can use any operator like +, -, / etc.
    b_list.append(new_item)
  print(b_list)#new list in output

mutate([1,2,3,5,8,13])#this list will change its value in an output
