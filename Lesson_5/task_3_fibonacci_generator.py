from typing import Generator, Optional, Union

class FibonacciGenerator:
    """Generates Fibonacci numbers."""

    def __init__(self):
        pass

    def generate_fibonacci(self, n_terms: Optional[int] = None) -> Generator[int, None, None]:
        """
        Generates Fibonacci numbers up to n_terms if specified, otherwise infinitely.
        The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, ...

        Args:
            n_terms: Optional. The number of Fibonacci terms to generate.
                     If None or non-positive, the generator will be infinite (or yield nothing if 0).

        Yields:
            int: The next Fibonacci number in the sequence.

        Raises:
            TypeError: If n_terms is not an integer or None.
        """
        if n_terms is not None and not isinstance(n_terms, int):
            raise TypeError("n_terms must be an integer or None.")

        a, b = 0, 1
        count = 0
        
        while True:
            if n_terms is not None and count >= n_terms:
                break
            yield a
            a, b = b, a + b
            count += 1

def main():
    """
    Main function to demonstrate the FibonacciGenerator.
    """
    fib_gen_instance = FibonacciGenerator()

    # Example 1: Generate the first 10 Fibonacci numbers
    print("--- First 10 Fibonacci numbers ---")
    try:
        fib_sequence_10 = fib_gen_instance.generate_fibonacci(n_terms=10)
        print(list(fib_sequence_10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    except TypeError as e:
        print(f"Error: {e}")
    print("\n")

    # Example 2: Generate the first 1 Fibonacci number
    print("--- First 1 Fibonacci number ---")
    try:
        fib_sequence_1 = fib_gen_instance.generate_fibonacci(n_terms=1)
        print(list(fib_sequence_1)) # [0]
    except TypeError as e:
        print(f"Error: {e}")
    print("\n")

    # Example 3: Generate 0 Fibonacci numbers (should yield nothing)
    print("--- 0 Fibonacci numbers ---")
    try:
        fib_sequence_0 = fib_gen_instance.generate_fibonacci(n_terms=0)
        print(list(fib_sequence_0)) # []
    except TypeError as e:
        print(f"Error: {e}")
    print("\n")

    # Example 4: Demonstrate potentially infinite generation (take first 15)
    print("--- First 15 numbers from the 'infinite' generator ---")
    try:
        infinite_gen = fib_gen_instance.generate_fibonacci() # n_terms is None
        first_15 = []
        for _ in range(15):
            first_15.append(next(infinite_gen))
        print(first_15)
        # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    except (TypeError, StopIteration) as e:
        print(f"Error: {e}")
    print("\n")

    # Example 5: Invalid n_terms type
    print("--- Invalid n_terms type (float) ---")
    try:
        fib_sequence_invalid = fib_gen_instance.generate_fibonacci(n_terms=5.5) # type: ignore
        print(list(fib_sequence_invalid))
    except TypeError as e:
        print(f"Error: {e}")
    print("\n")

if __name__ == "__main__":
    main() 