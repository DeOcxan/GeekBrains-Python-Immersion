import argparse
import datetime

class DateValidator:
    """Validates a given date."""

    def __init__(self):
        pass

    def is_leap_year(self, year: int) -> bool:
        """Checks if a year is a leap year."""
        if not isinstance(year, int):
            raise TypeError("Year must be an integer.")
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def is_date_valid(self, date_str: str, date_format: str = "%d.%m.%Y") -> bool:
        """
        Checks if a given date string is valid according to the specified format.
        Also performs logical date validation (day exists in month, considers leap years).

        Args:
            date_str: The date string to validate ("29.02.2024").
            date_format: The format of the date string (default: "%d.%m.%Y").

        Returns:
            True if the date is valid, False otherwise.
        """
        if not isinstance(date_str, str):
            # This would typically be caught by argparse type, but good for direct use
            print("Error: Date string must be a string.")
            return False

        try:
            # Try to parse the date string using datetime.strptime
            # This checks format والمبدئي (month between 1-12, day 1-31)
            dt_object = datetime.datetime.strptime(date_str, date_format)
            day, month, year = dt_object.day, dt_object.month, dt_object.year

            # Additional logical checks not fully covered by strptime (though strptime is quite good)
            # For example, strptime will allow 31.04.2023 but we want to catch it.
            # However, datetime.strptime already handles day/month/year ranges correctly.
            # The primary check using datetime.datetime.strptime is sufficient for most cases.
            # Let's confirm if manual day/month checks are needed post strptime for very old Pythons
            # For modern Python, strptime is robust.

            # The problem implies a custom check, let's explicitly check day ranges for month/year
            if month < 1 or month > 12:
                return False # Should be caught by strptime
            if day < 1 or day > 31: # Max days, refined below
                return False # Should be caught by strptime

            if month in [4, 6, 9, 11] and day > 30:
                return False
            elif month == 2:
                if self.is_leap_year(year):
                    if day > 29:
                        return False
                else:
                    if day > 28:
                        return False
            # For months with 31 days, day > 31 is already implicitly checked by strptime failing
            # or by the initial day range check.
            return True 
        except ValueError: # Catches format errors or invalid dates like 32.01.2023, 29.02.2023
            return False
        except TypeError as e:
            # This might happen if date_format is not a string, etc.
            print(f"Type error during date parsing: {e}")
            return False


def main():
    """
    Main function to parse command-line arguments and validate a date.
    """
    parser = argparse.ArgumentParser(description="Validate a date string.")
    parser.add_argument(
        "date_string", 
        type=str, 
        help="The date to check. Recommended format: DD.MM.YYYY (\"29.02.2024\")"
    )
    parser.add_argument(
        "--format", 
        type=str, 
        default="%d.%m.%Y", 
        help="The format of the date string (\"%%Y-%%m-%%d\"). Default is \"%%d.%%m.%%Y\"."
    )

    args = parser.parse_args()
    validator = DateValidator()

    print(f"Checking date: '{args.date_string}' with format '{args.format}'")
    if validator.is_date_valid(args.date_string, args.format):
        print(f"The date '{args.date_string}' is VALID.")
    else:
        print(f"The date '{args.date_string}' is INVALID.")

if __name__ == "__main__":
    # To run from terminal:
    # python task_1_date_validator.py "29.02.2024"
    # python task_1_date_validator.py "31.04.2023"
    # python task_1_date_validator.py "2023-12-20" --format "%Y-%m-%d"
    main() 