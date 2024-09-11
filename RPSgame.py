import random

def get_computer_choice():
  """generates a random choice for the computer"""
  choices = ["rock","paper","scissors"]
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  """determines the winner of the round"""
  if user_choice == computer_choice:
    return "It's a TIE!"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    return "You WIN!"
  else:
    return "Computer Wins!"

def play_game():
  """plays a round of rock paper scissors"""
  user_choice = input("Start the game(rock/paper/scissors): ").lower()
  computer_choice = get_computer_choice()
  print(f"Computer's move: {computer_choice}")
  result = determine_winner(user_choice, computer_choice)
  print(result)

if __name__ == "__main__":
  while True:
    play_game()
    play_again = input("Do you want to play again?(yes/no): ").lower()
    if play_again == "no":
      break
