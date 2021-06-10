import time
import sys 
import random

a = ["rock", "paper", "scissors"]  
rps = random.choice(a)
user=input("what would you like to choose(rock/paper/scissors) ")
print("Opponent choosing")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
if rps==user:
  print(f"Your Opponent Chose {rps}")
  print("draw")
elif rps=="paper" and user=="scissors":
  print("win")
  print(f"Your Opponent Chose {rps}")
elif rps=="scissors" and user=="rock":
  print("win")
  print(f"Your Opponent Chose {rps}")
elif rps=="scissors" and user=="paper":
  print("loss")
  print(f"Your Opponent Chose {rps}")
elif rps=="rock" and user=="paper":
  print("loss")
  print(f"Your Opponent Chose {rps}")
elif rps=="rock" and user == "scissors":
  print("win")
  print(f"Your Opponent Chose {rps}")
elif rps=="paper" and user=="rock":
  print("loss")
  print(f"Your Opponent Chose {rps}")
else:
  print("Your did not enter a valid answer. Run the program to try again. ")