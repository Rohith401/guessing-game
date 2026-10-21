import random
level=input("easy or hard?")
if level=="easy":
    maximum=50
else:
    maximum=200
secret=random.randint(1,maximum)
guess=0
tries=0
while guess!=secret:
    guess=int(input("guess a number from 1 to "+str(maximum)+":"))
    tries=tries+1
    if guess<secret:
        print("Too low")
    elif guess>secret:
        print("Too high")
    if guess==secret:
        print("Correct! you took",tries,"tries")    
    elif tries==8:      
        print("You lose")
        break
          
