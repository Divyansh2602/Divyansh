import random

count_zero = 0
count_one = 0

player_score = 0
computer_score = 0

def prediction():
  if count_zero > count_one:
    predict = 0
  elif count_one > count_zero:
    predict = 1
  else:
    predict = random.randint(0, 1)
  
  return predict

def update_counts(player_input):
  global count_zero, count_one
  if player_input == 0:
    count_zero = count_zero + 1
  else:
    count_one = count_one + 1

def update_scores(predicted, player_input):
  global player_score, computer_score
  if predicted == player_input:
    computer_score = computer_score + 1
    print("Computer Score:", computer_score)
    print("Player Score:", player_score)
  else:
    player_score = player_score + 1
    print("Computer Score:", computer_score)
    print("Player Score:", player_score)

def gameplay():
  valid_entries = ['0', '1']
  while True:
    # Get the predicted value and stored it in the 'predicted' variable.
    predicted = prediction()
    # Take input from the player and store it in the 'player_input' variable.
    player_input = input("Enter either 0 or 1: ")
    while player_input not in valid_entries:
      print("Invalid Input!")
      player_input = input("Please enter either 0 or 1: ")
    
    # Convert the 'player_input' value to an integer value.
    player_input = int(player_input)

    # Update the 'count_zero' and 'count_one' values using the 'update_counts()' function.
    update_counts(player_input)

    # Update the 'player_score' and 'computer_score' values using the 'update_scores()' function.
    update_scores(predicted, player_input)

    if player_score == 10:
      print("Congrats, You Won!")
      break
    elif computer_score == 10:
      print("Bad Luck, You Lost!")
      break

# Call the 'gameplay()' function to run the game.
gameplay()