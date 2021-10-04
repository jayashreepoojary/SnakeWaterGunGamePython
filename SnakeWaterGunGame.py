import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False  #you loose
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False  #you loose
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False  #you loose
        elif you == 'w':
            return True


#we also have to make sure that both the players choose at the same time, rather than choosing one after the other
print("Comp Turn: Snake(s) Water(w) or Gun(g) ?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: Snake(s) Water(w) or Gun(g) ?")


#game function will let us know who won
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose.")