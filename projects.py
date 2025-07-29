import random
count=0
all_roll_dice=[]    
while True:
    dice=input("Roll the dices ?(y/n):")
    #hi
    if(dice == 'y'):
        i=int(input("no of die you want to roll:"))
        for i in range(i):
            die1= random.randint(1,6) #radom num1 generated
            die2=random.randint(1,6) #random num2 generated
            result=(die1,die2)
            all_roll_dice.append(result)
            count=count+1
        print("\n all dice rolled")
        for i in range(len(all_roll_dice)):
            print(f"Roll{i+1}:{all_roll_dice[i]}")
        print(f"no of time you rolled dice: {count}")
    elif(dice == 'n'):
        print("Thanks for playing:") #if you choose n ,that mean end of the game
        break
    else:
        print("Invalid choice") 