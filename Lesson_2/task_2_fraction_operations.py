import fractions

class Fraction:
    """Represents a fraction with a numerator and a denominator."""

    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        common = self._gcd(abs(numerator), abs(denominator))
        self._numerator = numerator // common
        self._denominator = denominator // common

        if self._denominator < 0: # Ensure denominator is positive
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    def _gcd(self, a: int, b: int) -> int:
        """Computes the greatest common divisor of two integers."""
        while b:
            a, b = b, a % b
        return a

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            return NotImplemented # Or raise TypeError
        
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            return NotImplemented # Or raise TypeError

        new_numerator = self._numerator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    @classmethod
    def from_string(cls, fraction_str: str) -> 'Fraction':
        """Creates a Fraction object from a string like 'a/b'."""
        if not isinstance(fraction_str, str):
            raise TypeError("Input must be a string.")
        parts = fraction_str.split('/')
        if len(parts) != 2:
            raise ValueError("Fraction string must be in 'a/b' format.")
        try:
            num = int(parts[0])
            den = int(parts[1])
            return cls(num, den)
        except ValueError:
            raise ValueError("Numerator and denominator in 'a/b' string must be integers.")

def main():
    """
    Main function to get two fractions, perform operations, and print results.
    """
    try:
        frac_str1 = input("Enter the first fraction (a/b): ")
        frac1 = Fraction.from_string(frac_str1)
        
        frac_str2 = input("Enter the second fraction (a/b): ")
        frac2 = Fraction.from_string(frac_str2)

        # Custom implementation results
        sum_custom = frac1 + frac2
        prod_custom = frac1 * frac2
        print(f"\nCustom Implementation:")
        print(f"{frac1} + {frac2} = {sum_custom}")
        print(f"{frac1} * {frac2} = {prod_custom}")

        # Using Python's `fractions` module for verification
        py_frac1 = fractions.Fraction(frac1.numerator, frac1.denominator)
        py_frac2 = fractions.Fraction(frac2.numerator, frac2.denominator)
        
        sum_py = py_frac1 + py_frac2
        prod_py = py_frac1 * py_frac2
        print(f"\nPython's `fractions` module for verification:")
        print(f"{py_frac1} + {py_frac2} = {sum_py}")
        print(f"{py_frac1} * {py_frac2} = {prod_py}")

        # Verification
        print("\nVerification:")
        if sum_custom.numerator == sum_py.numerator and sum_custom.denominator == sum_py.denominator:
            print("Sum results match!")
        else:
            print(f"Sum results DO NOT match: Custom={sum_custom}, Python Lib={sum_py}")
        
        if prod_custom.numerator == prod_py.numerator and prod_custom.denominator == prod_py.denominator:
            print("Product results match!")
        else:
            print(f"Product results DO NOT match: Custom={prod_custom}, Python Lib={prod_py}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 