import random

number = int(input("Guess a positive number: "))

random_number = random.randint(0, number)

if number == random_number:
    print("Correct!")
else:
    print("Incorrect!")
    print(f"The correct number was {random_number}")