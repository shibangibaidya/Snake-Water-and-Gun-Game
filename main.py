'''
1 for Snake
-1 for water
0 for gun
'''
import random
choices=[-1,0,1]
computer=random.choice(choices)
# computer= -1
youstr =input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you= youDict[youstr]

# by now we have 2 number varibles you and computer

print(f"Computer choose: {reverseDict[computer]}")
print(f"You choose: {reverseDict[you]}")

you = youDict[youstr]

if(computer==you):
    print("It's a draw !")
else:
    if (computer==1 and you== -1 ):
        print("You Lose !")
    elif(computer==1 and you==0):
        print("You Win !")
    elif(computer==-1 and you==1):
        print("You Win !")
    elif(computer==-1 and you==0):
        print("You Lose !")
    elif(computer==0 and you==1):
        print("You Lose !")
    elif(computer==0 and you==-1):
        print("You Win !")
    else:
        print("Something Went Wrong !")