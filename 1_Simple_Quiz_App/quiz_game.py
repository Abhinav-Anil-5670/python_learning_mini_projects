print("Welcome to my Programming Quiz")

playing = input("Do you want to play? ").strip().lower()

if playing != "yes":
    quit()

print("Okay! Let's Play!")

score = 0

answer = input("What does JS stand for? ").strip().lower()

if answer == "javascript":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    print("The Answer is javascript")

answer = input("What does HTML stand for? ").strip().lower()

if answer == "hypertext markup language":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    print("The Answer is HyperText Markup Language")

answer = input("What does CSS stand for? ").strip().lower()

if answer == "cascading style sheets":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    print("The Answer is cascading style sheets")

answer = input("Which programming language is known for its readability and simplicity, often used for data analysis and machine learning? ").strip().lower()

if answer == "python":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    print("The Answer is Python")

answer = input("What is a piece of code that can be called by name and performs a specific task called? ").strip().lower()

if answer == "function":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    print("The Answer is function")
print(f"Total score is {score}/5")
