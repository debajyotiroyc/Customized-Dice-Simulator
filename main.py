#THIS IS A CUSTOM DICE SIMULATOR.
import random as rd

def easy_dice():
    values=[1,2,3,4,5,6]
    return(rd.choice(values))

def hard_dice():
    values=[1,2,3,4,5,6]
    new_values=rd.choices(values,weights=[5,5,2,1,1,1],k=20)
    if int(4) not in new_values:
        new_values.append(4)
    if int(5) not in new_values:
        new_values.append(5)
    if int(6) not in new_values:
        new_values.append(6)
    return (rd.choice(new_values))


name1,name2=input("Enter the name of the players: ").split()
level=input("Enter the difficulty level: Easy or Hard? ")

if level=="Easy":
    x="yes"
    while(x!="no"):
        print("Dice rolled for player "+name1+" and the dice points to: ")
        dice=easy_dice()
        print(dice)
        if dice==6:
            print("Since the dice points to value 6, player "+name1+" will have another go!")
            print("Dice rolled for player " + name1 + " and the dice points to: ")
            dice = easy_dice()
            print(dice)

        print("Dice rolled for player " + name2 + " and the dice points to: ")
        dice = easy_dice()
        print(dice)
        if dice == 6:
            print("Since the dice points to value 6, player " + name1 + " will have another go!")
            print("Dice rolled for player " + name2 + " and the dice points to: ")
            dice = easy_dice()
            print(dice)
        x=input("Do you wish to continue? ")
elif level=="Hard":
    x = "yes"
    while (x != "no"):
        print("Dice rolled for player " + name1 + " and the dice points to: ")
        dice = hard_dice()
        print(dice)
        if dice == 6:
            print("Since the dice points to value 6, player " + name1 + " will have another go!")
            print("Dice rolled for player " + name1 + " and the dice points to: ")
            dice = hard_dice()
            print(dice)

        print("Dice rolled for player " + name2 + " and the dice points to: ")
        dice = hard_dice()
        print(dice)
        if dice == 6:
            print("Since the dice points to value 6, player " + name1 + " will have another go!")
            print("Dice rolled for player " + name2 + " and the dice points to: ")
            dice = hard_dice()
            print(dice)
        x = input("Do you wish to continue? ")

print("\nDice Simulator was terminated. Hope you guys had fun playing!!!")


