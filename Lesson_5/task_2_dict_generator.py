from typing import List, Dict, Union

class SalaryCalculator:
    """Calculates bonus amounts and generates a dictionary of names to bonus amounts."""

    def __init__(self):
        pass

    def _parse_percentage_string(self, percent_str: str) -> float:
        """Converts a percentage string like '10.25%' to a float like 0.1025."""
        if not isinstance(percent_str, str) or not percent_str.endswith('%'):
            raise ValueError(f"Invalid percentage string format: '{percent_str}'. Expected 'value%'.")
        try:
            return float(percent_str.rstrip('%')) / 100.0
        except ValueError:
            raise ValueError(f"Could not convert percentage value to float: '{percent_str.rstrip('%')}'.")

    def create_bonus_dictionary(self, names: List[str], rates: List[Union[int, float]], 
                                bonuses_percent_str: List[str]) -> Dict[str, float]:
        """
        Takes three lists: names, rates, and bonus percentage strings.
        Returns a dictionary with names as keys and calculated bonus amounts as values.
        The bonus amount is rate * (bonus_percentage / 100).
        Uses a dictionary comprehension as required.

        Args:
            names: A list of names (str).
            rates: A list of salary rates (int or float).
            bonuses_percent_str: A list of bonus percentages as strings ("10.25%").

        Returns:
            A dictionary where keys are names and values are the calculated bonus amounts.

        Raises:
            ValueError: If the input lists are not of the same length or other parsing errors.
            TypeError: If input types are incorrect.
        """
        if not (isinstance(names, list) and isinstance(rates, list) and isinstance(bonuses_percent_str, list)):
            raise TypeError("All inputs (names, rates, bonuses_percent_str) must be lists.")
        
        if not (len(names) == len(rates) == len(bonuses_percent_str)):
            raise ValueError("Input lists (names, rates, bonuses_percent_str) must be of the same length.")

        if not all(isinstance(name, str) for name in names):
            raise TypeError("All items in 'names' list must be strings.")
        if not all(isinstance(rate, (int, float)) for rate in rates):
            raise TypeError("All items in 'rates' list must be integers or floats.")
        if not all(isinstance(bonus_str, str) for bonus_str in bonuses_percent_str):
            raise TypeError("All items in 'bonuses_percent_str' list must be strings.")

        # Dictionary comprehension for the core logic
        # The parsing of percentage string is done inside the comprehension by calling a helper,
        # or it could be pre-processed. For a strict "one-liner generator" feel, this is okay.
        # Error handling for parsing will occur during the comprehension if not pre-validated.
        try:
            bonus_dict = {name: rate * self._parse_percentage_string(bonus_str) 
                          for name, rate, bonus_str in zip(names, rates, bonuses_percent_str)}
        except ValueError as e: # Catch parsing errors from _parse_percentage_string
            raise ValueError(f"Error during dictionary generation: {e}")
        
        return bonus_dict

def main():
    """
    Main function to demonstrate the SalaryCalculator.
    """
    calculator = SalaryCalculator()

    names1 = ["Alice", "Bob", "Charlie"]
    rates1 = [50000, 60000, 75000]
    bonuses1 = ["10%", "12.5%", "15.25%"]
    
    print(f"--- Case 1 ---")
    print(f"Names: {names1}")
    print(f"Rates: {rates1}")
    print(f"Bonuses (str): {bonuses1}")
    try:
        result_dict1 = calculator.create_bonus_dictionary(names1, rates1, bonuses1)
        print(f"Bonus Dictionary: {result_dict1}\n")
        # Expected: Alice: 5000.0, Bob: 7500.0, Charlie: 11437.5
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

    names2 = ["David"]
    rates2 = [100000]
    bonuses2 = ["0.0%"]
    print(f"--- Case 2 (Zero Bonus) ---")
    try:
        result_dict2 = calculator.create_bonus_dictionary(names2, rates2, bonuses2)
        print(f"Bonus Dictionary: {result_dict2}\n")
        # Expected: David: 0.0
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

    names3 = []
    rates3 = []
    bonuses3 = []
    print(f"--- Case 3 (Empty Lists) ---")
    try:
        result_dict3 = calculator.create_bonus_dictionary(names3, rates3, bonuses3)
        print(f"Bonus Dictionary: {result_dict3}\n")
        # Expected: {}
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

    # Error case: mismatched list lengths
    names_err1 = ["Eve", "Frank"]
    rates_err1 = [80000]
    bonuses_err1 = ["5%"]
    print(f"--- Case 4 (Mismatched List Lengths) ---")
    try:
        result_dict_err1 = calculator.create_bonus_dictionary(names_err1, rates_err1, bonuses_err1)
        print(f"Bonus Dictionary: {result_dict_err1}\n")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

    # Error case: invalid percentage string
    names_err2 = ["Grace"]
    rates_err2 = [90000]
    bonuses_err2 = ["invalid_bonus_str"]
    print(f"--- Case 5 (Invalid Bonus String) ---")
    try:
        result_dict_err2 = calculator.create_bonus_dictionary(names_err2, rates_err2, bonuses_err2)
        print(f"Bonus Dictionary: {result_dict_err2}\n")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

    # Error case: non-numeric rate (should be caught by type checks)
    names_err3 = ["Heidi"]
    rates_err3 = ["not_a_rate"] # type: ignore
    bonuses_err3 = ["7.5%"]
    print(f"--- Case 6 (Invalid Rate Type) ---")
    try:
        result_dict_err3 = calculator.create_bonus_dictionary(names_err3, rates_err3, bonuses_err3)
        print(f"Bonus Dictionary: {result_dict_err3}\n")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

if __name__ == "__main__":
    main() 