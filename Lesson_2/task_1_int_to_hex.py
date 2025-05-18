def to_hex_custom(number: int) -> str:
    """
    Converts an integer to its hexadecimal string representation.
    Handles positive integers, zero, and negative integers (using two's complement for simplicity for display).
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number == 0:
        return "0x0"

    hex_chars = "0123456789abcdef"
    hex_string = ""
    
    # For simplicity, let's work with the absolute value for negative numbers
    # and add the sign later, or one could implement two's complement for a fixed bit size.
    # The built-in hex() for negative numbers returns -0x..., which is a common representation.
    prefix = "0x"
    if number < 0:
        prefix = "-0x"
        number = abs(number)

    while number > 0:
        remainder = number % 16
        hex_string = hex_chars[remainder] + hex_string
        number //= 16
    
    return prefix + hex_string

def main():
    """
    Main function to get integer input and print its hex representation.
    """
    try:
        num_str = input("Enter an integer: ")
        num = int(num_str)

        custom_hex_representation = to_hex_custom(num)
        builtin_hex_representation = hex(num)

        print(f"Custom function hex: {custom_hex_representation}")
        print(f"Built-in hex function: {builtin_hex_representation}")

        if custom_hex_representation == builtin_hex_representation:
            print("Results match!")
        else:
            # This might happen for negative numbers if a different representation ( two's complement) is expected
            # or if my custom function has a slight difference in how it handles the prefix for negative numbers.
            # The built-in hex() returns '-0x...' for negative numbers.
            print("Results differ. Note: Built-in hex() for negative numbers uses a specific format.")
            print("My custom function aims for a similar prefix style for negative numbers.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 