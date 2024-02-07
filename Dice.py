import random

print("=====..... Computer is rolling the dice .....=====")

DiceComp = random.randint(1, 6)
# print(DiceComp)

GameType = ['1. Run 100 M', '2. Jump five times from place darer likes.', '3. Write an essay on India.',
            '4. Give party to your friends.', '5. Go on trip with your friends.', '6. Go and watch movie.']

if DiceComp == 1:
    print("------------")
    print("|    *     |")
    print("------------")
    print(f"Dice Rolled and give you number : {DiceComp}")


elif DiceComp == 2:
    print("------------")
    print("|    * *    |")
    print("------------")
    print(f"Dice Rolled and give you number : {DiceComp}")

elif DiceComp == 3:
    print("------------")
    print("|    * * *    |")
    print("------------")
    print(f"Dice Rolled and give you number : {DiceComp}")

elif DiceComp == 4:
    print("------------")
    print("|    * *     |")
    print("|    * *     |")
    print("------------")
    print(f"Dice Rolled and give you number : {DiceComp}")


elif DiceComp == 5:
    print("------------")
    print("|    * *     |")
    print("|     *      |")
    print("|    * *     |")
    print("------------")
    print(f"Dice Rolled and give you number : {DiceComp}")

elif DiceComp == 6:
    print("------------")
    print("|    * *     |")
    print("|    * *     |")
    print("|    * *     |")
    print("------------")
    print(f"Dice Rolled and give you number : {DiceComp}")

print(f"Your Dare is :- {GameType}")

print("------>> Thankyou for playing this game :)")
