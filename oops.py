
import random

target = random.randint(1,100)

while True:
    guess = int(input("Guess the number: "))
    if guess == target:
        print("You guessed it!")
        break
    elif guess < target:
        print("Too low")
    else:
        print("Too high")