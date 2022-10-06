"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
# import the random package
import random

high_score = 0

# function to start the game
def start_game():

  global high_score

  # variable to store guess attempts
  guess_attempts = 0

  # store a random integer between 1 and 10 in a variable
  random_num = random.randint(1, 10)
  
  # display a welcome message
  print("*** Welcome to the Number Guessing Game! ***")
  if high_score > 0:
    print("The current High Score is {} attempts! Good Luck!".format(high_score))


  # loop while the player's guess is incorrect
  while True:

    try:
      # prompt player to guess the number
      player_input = input(">>> Try to guess the number! (It's between 1 and 10): ")
      player_guess = int(player_input)
      # if player guesses a number outside of 1-10...
      if player_guess <= 0 or player_guess > 10:
        raise Exception("Please enter a number between 1 & 10.")
    # if player enters something other than a number...
    except ValueError:
      print("Please enter a number.")
      guess_attempts += 1
      continue
    except Exception as e:
      print(e)
      guess_attempts += 1
      continue
    else:
      # if the guess is too high...
      if player_guess > random_num:
        print("It's LOWER. Try again...")
        guess_attempts += 1
        continue
      # if the guess is too low...
      elif player_guess < random_num:
        print("It's HIGHER. Try again...")
        guess_attempts += 1
        continue
    break  
  # if the guess was correct...
  guess_attempts += 1
  print("You got it! The number was {}!".format(random_num))
  print("It took you {} tries to guess it!".format(guess_attempts))

  # set new high score if it's lower than the current.
  if guess_attempts < high_score or high_score == 0:
    high_score = guess_attempts

  # prompt player to play again
  play_again = input(">>> Would you like to play again? (yes / no) ")
  
  if play_again.lower() == "yes":
    start_game()
  else:
    print("Thanks for playing!")
# Kick off the program by calling the start_game function.
start_game()