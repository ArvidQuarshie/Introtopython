import random

def roll(sides=6):
    num_rolled=random.randint(1,sides)
    return num_rolled


    sides=6
    rolling=True
    while rolling:
        roll_again=input("ready to roll? Enter=ROll. Q=Quit")
    if roll_again.lower() != "q":
        num_rolled=roll(sides)
        print("you rolled a " ,num_rolled)
    else:
        rolling=False

    
    print ("Thanks For Playing")
