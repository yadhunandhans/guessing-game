import random
print("Welcom To Number Guessing Game")
Random_Number=random.randint(1, 100)
print("Find The Guess Number Between 1 To 100= " )
attempts=0
while True:
    Guess_Number = int(input())
    attempts=attempts+1
    if(Random_Number>Guess_Number):
        print("Value Is High")
    elif(Random_Number<Guess_Number):
        print("Value Is Less")
    else:
        print("Guess Number Is Correct")
    

