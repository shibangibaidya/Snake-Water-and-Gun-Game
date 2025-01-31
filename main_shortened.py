import random

choices=[-1,0,1]
computer=random.choice(choices)

youstr=input("Enter you input: 's' for snake,'w' for water,'g' for gun: ")
youDict={'s':1,'w':-1,'g':0}
reverseDict={1:'Snake',-1:'Water',0:'Gun'}

you = youDict[youstr]

print(f"Computer Choose: {reverseDict[computer]}\nYou Choose: {reverseDict[you]}")


if(computer==you):
    print("It's a Draw !")
else:
    if(computer-you==2 or computer-you==-1):
        print("You Lose !")
    elif(computer-you==1 or computer-you==-2):
        print("You Win !")
    else:
        print("Something Went Wrong :(  !!! ")







# if(computer==you):
#     print("It's a draw !")
# else:
#     if (computer==1 and you== -1 ):   c-y=1-(-1)=2
#         print("You Lose !")
#     elif(computer==1 and you==0):     c-y=1-0=1
#         print("You Win !")
#     elif(computer==-1 and you==1):    c-y=-1-1=-2
#         print("You Win !")
#     elif(computer==-1 and you==0):    c-y=-1-0=-1
#         print("You Lose !")
#     elif(computer==0 and you==1):     c-y=0-1=-1
#         print("You Lose !")
#     elif(computer==0 and you==-1):    c-y=0-(-1)=1
#         print("You Win !")
#     else:
#         print("Something Went Wrong !")