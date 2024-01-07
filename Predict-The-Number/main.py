from art import logo

print(logo)
print("Welcome to Predict The Number!\nI'm thinking of a number between 1 to 100.")

import random

num = random.randint(1,100)
print(num)

game_diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_diff.lower() == 'hard':
  attempts = 5
else:
  attempts = 10

def num_prediction(a):
  b = 1
  lh1 = "Yes"
  lh2 = "No"
  
  if num > a:
    lh1 = "High"
  elif num < a:
    lh1 = "Low"
  else:
    b = 3

  if abs(num-a) != 0:
    if abs(num-a) <= 10:
      lh2 = "Little"
    elif abs(num-a) <= 30:
      lh2 = lh1
    elif abs(num-a) <= 60:
      b = 2
      lh2 = "Enough"
    else:
      lh2 = "Too"

  if lh1 != lh2 and b == 1:
    lh = lh2 + " " + lh1
  elif lh1 != lh2 and b != 1:
    lh = lh1 + " " + lh2
  else:
    lh = lh1

  return lh

def end_game():
  if attempts != 0 and attempts != 1:
    print(f"You predicted the number! You win with {attempts} attempts remaining.")
  elif attempts != 0:
    print(f"You predicted the number! You win with {attempts} attempt remaining.")
  else:
    print(f"You've run out of attempts. You lose. The number was {num}.")

while attempts>0:
  if attempts !=1:
    print(f"You have {attempts} attempts remaining.")
    num_predict = int(input("Make the prediction: "))
  else:
    print(f"This is you last prediction.")
    num_predict = int(input("Make this prediction wisely: "))


  res = num_prediction(num_predict)
  if res  == "Yes No":
    end_game()
    attempts = 0
  else:
    print(f"Go {res}")


  attempts -= 1

  if attempts == 0:
    end_game()
