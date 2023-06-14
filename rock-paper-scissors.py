# Image for rock
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Image for paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# Image for scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# importing random module
# Made CPU an opponent for the user and made a list of the three options for Rock, Paper, Scissors.
cpu_options = [rock, paper, scissors]
# Randomising the options for the cpu on every game.
cpu_picks = random.choice(cpu_options)
# Input for the user to choose Rock, Paper or Scissors
options = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# If the user selects rock, theses are the outcomes.
if options == "0" and cpu_picks == rock:
    print(
        f"You chose rock {rock}\n Computer Chose: rock \n {rock}\n You Both Draw.")
elif options == "0" and cpu_picks == paper:
    print(
        f"You chose rock {rock}\n Computer Chose: paper \n {paper}\n You Lose.")
elif options == "0" and cpu_picks == scissors:
    print(
        f"You chose rock {rock}\n Computer Chose: scissors \n {scissors}\n You Win.")

# If the user selects paper, theses are the outcomes.
if options == "1" and cpu_picks == rock:
    print(
        f"You chose paper {paper}\n Computer Chose: rock \n {rock}\n You Win.")
elif options == "1" and cpu_picks == paper:
    print(
        f"You chose paper {paper}\n Computer Chose: paper \n {paper}\n You Both Draw.")
elif options == "1" and cpu_picks == scissors:
    print(
        f"You chose paper {paper}\n Computer Chose: scissors \n {scissors}\n You Lose.")

# If the user selects scissors, theses are the outcomes.
if options == "2" and cpu_picks == rock:
    print(
        f"You chose scissors {scissors}\n Computer Chose: rock\n {rock}\n You Lose.")
elif options == "2" and cpu_picks == paper:
    print(
        f"You chose scissors {scissors}\n Computer Chose: paper \n {paper}\n You Win.")
elif options == "2" and cpu_picks == scissors:
    print(
        f"You chose scissors {scissors}\n Computer Chose: scissors \n {scissors}\n You Both Draw..")
