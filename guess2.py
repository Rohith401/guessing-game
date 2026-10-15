import random
secret=random.randint(1,10)
guess=0
tries=0
while guess!=secret:
    guess=int(input("guess a number from 1 to 10:"))
    tries=tries+1
    if guess<secret:
        print("Too low")
    elif guess>secret:
        print("Too high")
print("Correct! you took",tries,"tries")        
