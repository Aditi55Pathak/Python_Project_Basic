import random

# Game Rule for Rock, paper, sissor game.


def gameRule(computer, player):

    # If two values are equal, declare a tie!

    if computer == player:
        return None

    # All propablities for Sissor

    elif computer == 's':
        if player == 'p':
            return False
        elif player == 'r':
            return True

    # All propablities for Paper

    elif computer == 'p':
        if player == 'r':
            return False
        elif player == 's':
            return True

    # All propablities for Rock

    elif computer == 'r':
        if player == 's':
            return False
        elif player == 'p':
            return True


print("Computer's Turn:- Sissor(s), Paper(p), Rock(r) ")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'p'
elif randNo == 3:
    computer = 'r'

player = input("Computer's Turn:- Sissor(s), Paper(p), Rock(r) :- ")
a = gameRule(computer, player)

print(f"Computer chose {computer}")
print(f"Player chose {player}")

if a == None:
    print("The game is a tie !!!")
elif a:
    print("PLAYER Win this game :)")
else:
    print("PLAYER Lose this game :<(")
