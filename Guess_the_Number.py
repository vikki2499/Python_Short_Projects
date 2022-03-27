import random


top_of_range = input("Type the Number: ")
if top_of_range.isdigit():
    top_of_range= int(top_of_range)
    if(top_of_range<=0):
        print("Please type a number greater than 0")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number = random.randrange(11)
guess_count = 0

while True:
    guess_count+=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == random_number:
        print("You guessed it correct!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")        
print("You guessed the number in"+ str(guess_count) +"guesses :)")