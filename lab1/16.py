def guess_the_number(secret_number):
    print("Player 2, you have 3 chances to guess the secret number.")
    for _ in range(3):
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! You guessed the secret number!")
            return
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    print("Sorry, you have run out of guesses. The secret number was:", secret_number)

secret_number = int(input("Player 1, enter the secret number: "))
print("\n" * 100)  # Clear screen
guess_the_number(secret_number)
