print("Welecome to Treasure Island!\n Your mission is to find the treasure. Good Luck!")
crossroads=input("You are at the cross roads. DO you want to move left or right?")
if(crossroads=="right"):
    print("GAME OVER!!!")
else:
    lake=input("You have reached the lake.Are you waiting for the boat or swimming?")
    if(lake=="swim"):
        print("GAME OVER!!!")
    else:
        door=input("You have succesfully reached the castle.There are three doors infront of you.Red,Blue and Yellow.Which one do you choose?")
        if(door=="Red"):
            print("Oh no the dragon has seen you, it's breathing fire, and you are dead.\nGAME OVER")
        elif(door=="Blue"):
            print("Oh no the assassin has spotted you. He is swinging his blade, and you are dead.\nGAME OVER")
        else:
            print("There sits the treasure. You have found it. Congratulations little warrior, you have found the treasure.!!!")
