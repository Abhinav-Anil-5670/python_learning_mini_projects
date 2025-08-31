import random

top_of_range = input("Enter a Number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please a number greater than 0")
        quit()
else:
    print("Please enter a number")
    quit()

random_number = random.randint(0,top_of_range)
number_of_guess = 0

while True:
    number_of_guess +=1
    guess  = input("Guess the Number ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please,Enter a Number")
        continue


    if guess == random_number:
        if number_of_guess == 0 :
            print(f"You guessed the number correctly the first time. The number was {random_number}")
        else:
            print(f"You guessed the number correctly. It was {random_number}")
            print(f"You took {number_of_guess} tries, to guess the number")
        break
    else:
        
        print("You got it wrong... Try again")