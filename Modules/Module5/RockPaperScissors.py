import random
print('Rock Paper Scissors Game')
rps=["Rock","Paper","Scissors"]
pChoice=input('Choose one: Rock, Paper or Scissors!\n ')
cChoice=random.choice(rps)
print('Computer chooses: ' + str(cChoice))
if cChoice == str('Paper') and pChoice == ('Paper'):
    print('Tied!')
if cChoice == str('Paper') and pChoice == ('Rock'):
    print('Computer wins!')
if cChoice == str('Paper') and pChoice == ('Scissors'):
    print('Player wins!')

if cChoice == str('Rock') and pChoice == ('Rock'):
    print('Tied!')
if cChoice == str('Rock') and pChoice == ('Paper'):
    print('Player wins!')
if cChoice == str('Rock') and pChoice == ('Scissors'):
    print('Computer wins!')

if cChoice == str('Scissors') and pChoice == ('Scissors'):
    print('Tied!')
if cChoice == str('Scissors') and pChoice == ('Paper'):
    print('Computer wins!')
if cChoice == str('Scissors') and pChoice == ('Rock'):
    print('Player wins!')
    