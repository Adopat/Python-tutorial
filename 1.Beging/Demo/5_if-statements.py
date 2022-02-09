# a simple game
age = 24
print("Guess my age,you have 1 chances!")
guess = int(input("Enter your guess:"))
if guess != age:
    print("You are wrong")
else:
    print("You are Correct")
