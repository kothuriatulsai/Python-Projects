from data import data
import random
from art import logo
from art import vs


def dict():
  return random.choice(data)


def statement(dict):
  name = dict["name"]
  description = dict["description"]
  country = dict["country"]
  st = f"{name}, a {description}, from {country}"
  return st


def check_answer(guess, fc_a, fc_b):
  if fc_a > fc_b:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_continue = True
  a = dict()
  b = dict()

  while game_continue:
    a = b
    b = dict()

    while a == b:
      b = dict()

    print(f"Compare A: {dict(a)}.")
    print(vs)
    print(f"Against B: {dict(b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    fc_a = a["follower_count"]
    fc_b = b["follower_count"]
    check = check_answer(guess, fc_a, fc_b)

    print()
    print()
    print()
    if check:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")


game()
