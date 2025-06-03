import random

computer_number_to_guess= random.randint(1,100)
attempts=0

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 to 100")

while True:
    guess_input=(input("Enter your guess number: "))

    if guess_input.isdigit():
        guess=int(guess_input)
        attempts+=1

        if guess < computer_number_to_guess:
            print("Your number is less than the actual number. Try Again!")
        elif guess> computer_number_to_guess:
            print("Your number is greater than the actual nmber. Try Again!")
        else: 
            print(f"Congratulations! You have guessed the number correct in {attempts} attempts")
            break
    else:
        print("Invalid input. Please enter a number")

