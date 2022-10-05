"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
# import the random package
import random

# function to start the game
def start_game():

  # variable to store guess attempts
  guess_attempts = 0

  # store a random integer between 1 and 10 in a variable
  random_num = random.randint(1, 10)
  
  # display a welcome message
  print("***Welcome to the Number Guessing Game!***")
  


  # loop while the player's guess is incorrect
  while True:

    try:
      # prompt player to guess the number
      player_guess = input(">>> Try to guess the number! (It's between 1 and 10): ")

      # if player guesses a number outside of 1-10...
      if int(player_guess) <= 0 or int(player_guess) > 10:
        raise Exception("Please enter a number between 1 & 10.")
    except ValueError:
      print("Please enter a number.")
      continue
    except Exception as e:
      print(e)
      guess_attempts += 1
      continue
    else:
      # if the guess is too high...
      if int(player_guess) > random_num:
        player_guess = input(">>> It's LOWER. Try again: ")
        guess_attempts += 1
      # if the guess is too low...
      elif int(player_guess) < random_num:
        player_guess = input(">>> It's HIGHER. Try again: ")
        guess_attempts += 1
    break  
  # if the guess was correct...
  print("You got it! The number was {}!".format(random_num))
  print("It took you {} tries to guess it!".format(guess_attempts))
  
# Kick off the program by calling the start_game function.
start_game()