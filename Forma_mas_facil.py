#Proyecto final
#importar el modulo random
import random
#variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Para que el usuario ingrese su opcion
usuario = input("What do you choose? type 0 for Rock, 1 for paper and 2 for Scissors.\n")
computadora = random.randint(0,2)
if  usuario == "0"  and computadora == 0:
    print("You choose Rock")
    print(rock)  #usuario piedra
    print("Computer choose Rock")
    print(rock)  #computadora piedra
    print("it´s a draw")
elif usuario == "0" and computadora == 1:
    print("You choose Rock")
    print(rock)
    print("Computer choose Paper")
    print(paper)
    print("You win")
elif usuario == "0" and computadora == 2:
    print("You choose Rock")
    print(rock)
    print("Computer choose Scissors")
    print(scissors)
    print("You win")
elif  usuario == "1"  and computadora == 0:
    print("You choose Paper")
    print(paper)
    print("Computer choose Rock")
    print(rock)
    print("The computer win")
elif usuario == "1" and computadora == 1:
    print("You choose Paper")
    print(paper)
    print("Computer choose Paper")
    print(paper)
    print("It´s a draw")
elif  usuario == "1"  and computadora == 2:
    print("You choose Paper")
    print(paper)
    print("Computer choose Scissors")
    print(scissors)
    print("The computer win")
elif  usuario == "2"  and computadora == 0:
    print("You choose Scissors")
    print(scissors)
    print("Computer choose Rock")
    print(rock)
    print("The computer win")
elif usuario == "2" and computadora == 1:
    print("You choose Scissors")
    print(scissors)
    print("Computer choose Paper")
    print(paper)
    print("You win")
elif  usuario == "2"  and computadora == 2:
    print("You choose Scissors")
    print(scissors)
    print("Computer choose Scissors")
    print(scissors)
    print("It´s a draw")