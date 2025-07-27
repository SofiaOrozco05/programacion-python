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
if usuario == "0":
    print("You choose Rock")
    print(rock) #si el usuario escribe 0 se imprime piedra
elif usuario == "1":
    print("You choose Paper")
    print(paper) ##si el usuario escribe 1 se imprime papel
elif usuario == "2":
    print("You choose Scissors")
    print(scissors)  ##si el usuario escribe 1 se imprime papel
else:
    print("please type a correct number")
    exit()
#Lo que escogera la laptop
computadora = random.randint(0,2) #llama a la funcion randint para que escoga un numero aleatorio
# que este dentro del rango de 0 a 2
if computadora == 0:#si el numero es 0
    print("Computer choose Rock")
    print(rock)
elif computadora == 1: #si el numero es 1
    print("Computer choose Paper")
    print(paper)
else:
    print("Computer choose Scissors")
    print(scissors)

#para ver quien gano
if  usuario == "0"  and computadora == 0:
     print("it´s a draw")
elif usuario == "0" and computadora == 1:
     print("You win")
elif usuario == "0" and computadora == 2:
     print("You win")
if  usuario == "1"  and computadora == 0:
     print("The computer win")
if usuario == "1" and computadora == 1:
         print("It´s a draw")
if  usuario == "1"  and computadora == 2:
     print("The computer win")
if  usuario == "2"  and computadora == 0:
     print("The computer win")
if usuario == "2" and computadora == 1:
         print("You win")
if  usuario == "2"  and computadora == 2:
     print("It´s a draw")