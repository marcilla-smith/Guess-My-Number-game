import random
r = random.randint(1, 100)
while r:
    g = input("Please guess a number between 1 and 100 (inclusive):")
    g = int(g)
    if g == r:
        print("You are right, great job")
        break
    elif g < r:
        print("Your guess is low, try again!")
    elif g > r:
        print("Your guess is high, try again!")
    else:
        print("are you sure that's a number?")
