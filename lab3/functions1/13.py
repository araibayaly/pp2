import random 
name = str(input("Hello! What is your name?"))

print("Well, " + name + ", I am thinking of a number between 1 and 20.")
num=random.randint(1,20)
n=0
g=0
while n!=num:
    n = int(input("Take a guess."))
    g += 1
    if n<num:
        print("Your guess is too low.")
    elif n>num:
        print("Your guess is too high.")
print(f"Good job, {name}! You guessed my number in {g} guesses! ") 

