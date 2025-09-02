name = input("Enter Your Name:")
print("Welcome,",name,"to this adventure")

answer = input("You are at the end of the road. You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You walk down the left path, the air grows damp and heavy. Soon, you reach a roaring river. Do you want to walk across the bank to find another way or swim across? ").lower()
    if answer == "swim":
        print("The current is stronger than you expected. As you fight to stay afloat, an alligator rises from the depths and drags you under. Your story ends here.")
    elif answer == "walk":
        print("You walk along the endless riverbank for miles, your feet blistered and body aching. No crossing appears, and exhaustion takes your life. You collapse, forgotten by the world.")
    else:
        print("Not a valid option")

elif answer == "right":
    answer = input("The path twists into shadows, leading to a bridge hanging over a dark chasm. The wood creaks under the faint wind. Do you want to cross or go back? ").lower()
    if answer == "cross":
        answer = input("You step onto the bridge, each board moaning under your weight. Halfway across, you hear something snap. Do you run or stay calm and walk carefully? ").lower()
        if answer == "run":
            print("You sprint, but the bridge gives way beneath you. You plunge into the darkness below, your screams swallowed by the void.")
        elif answer == "walk":
            print("You steady yourself and walk carefully. The boards groan but hold. On the other side, you find an abandoned village, its houses silent and hollow. As you explore, shadows move among the ruins. You realize you are not alone.")
        else:
            print("Not a valid option")
    elif answer == "back":
        print("You turn back, retracing your steps. But the forest has shifted, and the path is no longer the same. You wander endlessly, trapped in a maze of trees until despair takes you.")
    else:
        print("Not a valid option")

else:
    print("Not a valid option")
