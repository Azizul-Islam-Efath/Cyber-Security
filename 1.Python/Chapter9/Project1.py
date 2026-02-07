import random

'''
1 for Snake
-1 for Water
0 for Gun

Snake Drinks Water
Gun Kill Snakes
Gun sinks into the water
'''

computer=random.choice([-1,0,1])

DefinedStr={"S":1,"W":-1,"G":0}
Display_Stake={1:"Snake",-1:"Water",0:"Gun"}

Your_INPUT=input("Choose One From ...(  S | W | G  )\n")

You=DefinedStr[Your_INPUT]

print(f"You have choosed {Display_Stake[You]} \n\n\nComputer have choosed {Display_Stake[computer]}\n\n")

if(computer==You):
    print("Match Draw.")
else:
    if(computer==1 and You==0):
        print("Yeaaaaaa..You Win..!")
    elif(computer==1 and You==-1):
        print("Sorry😢..You have Lost..!")
    elif(computer==-1 and You==0):
        print("Sorry😢..You have Lost..!")
    elif(computer==-1 and You==1):
        print("Yeaaaaaa..You Win..!")
    elif(computer==0 and You==-1):
        print("Yeaaaaaa..You Win..!")
    elif(computer==0 and You==1):
        print("Sorry😢..You have Lost..!")
    else:
        print("Something went wrong.Try With Valid Inputs...(0 / -1 / 1)")
    