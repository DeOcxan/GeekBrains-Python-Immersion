from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

def play_guessing_game():
    """
    Manages the number guessing game.
    The program generates a random number, and the user tries to guess it.
    """
    secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts_left = MAX_ATTEMPTS

    print(f"I have guessed a number between {LOWER_LIMIT} and {UPPER_LIMIT}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.")

    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")
        try:
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)

            if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
                print(f"Please enter a number between {LOWER_LIMIT} and {UPPER_LIMIT}.")
                continue # Does not count as an attempt

            attempts_left -= 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {MAX_ATTEMPTS - attempts_left} attempt(s).")
                return
            elif guess < secret_number:
                print("My number is greater.")
            else: # guess > secret_number
                print("My number is lesser.")
        
        except ValueError:
            print("Invalid input. Please enter an integer.")
            # Optionally, you could choose not to decrement attempts_left here
            # but the problem description doesn't specify, so we'll count it.

    print(f"\nSorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    play_guessing_game() 