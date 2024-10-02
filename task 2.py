import random

def guess_the_number():
   
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    
    while not guessed_correctly:
        
        user_guess = input("Enter your guess: ")

        
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1

       
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
            print(f"It took you {attempts} attempts to guess the number.")

guess_the_number()
