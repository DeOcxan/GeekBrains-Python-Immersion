def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    A number is prime if it is divisible only by 1 and itself.
    """
    if n <= 1:
        return False
    if n <= 3: # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0: # Divisible by 2 or 3
        return False
    # Check from 5 onwards, with a step of 6 (i.e., 5, 11, 17, ...)
    # All primes greater than 3 are of the form 6k ± 1.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    """
    Main function to get number input, validate, and check for primality.
    """
    MAX_LIMIT = 100000
    MIN_LIMIT = 0 # Technically, prime numbers are > 1

    try:
        num_str = input(f"Enter an integer (greater than {MIN_LIMIT} and not more than {MAX_LIMIT}): ")
        num = int(num_str)

        if num <= MIN_LIMIT:
            print(f"Input number must be greater than {MIN_LIMIT}.")
            return
        if num > MAX_LIMIT:
            print(f"Input number must not be greater than {MAX_LIMIT}.")
            return
        
        if num == 1: # Special case for 1
             print(f"{num} is neither prime nor composite.")
        elif is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is a composite number.")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main() 