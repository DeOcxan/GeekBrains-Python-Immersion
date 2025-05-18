# GeekBrains Python Immersion Coursework

This repository contains the solutions for the Python Immersion course assignments at GeekBrains. Each lesson's tasks are organized into respective directories.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DeOcxan/GeekBrains-Python-Immersion.git
    cd GeekBrains-Python-Immersion
    ```

2.  **Navigate to a specific lesson directory:**
    ```bash
    cd Lesson_X 
    ```
    (Replace `X` with the lesson number, `Lesson_1`)

3.  **Run a task script:**
    Most task files (`task_Y_*.py`) are designed to be run directly.
    ```bash
    python task_Y_description.py
    ```
    (Replace `Y` with the task number and `description` with its name, `python task_1_triangle.py`)

4.  **Explore packages:**
    *   For `Lesson_6/chess_package` and `Lesson_7/file_management_package`, you can import and use the classes/functions within your own Python scripts or an interactive Python session. Refer to the `__init__.py` files and the example usage within the task files (like `Lesson_7/task_1_batch_rename.py`) for guidance.

5.  **Dependencies:**
    *   This project primarily uses Python 3.11 and its standard library.
    *   No external packages requiring `pip install` are used in the current tasks. If future tasks introduce external dependencies, they will be noted.

## Tech Stack
- Python 3.11
- Standard Python Libraries (including but not limited to: `os`, `sys`, `random`, `collections`, `datetime`, `fractions`, `argparse`, `math`, `re`, `itertools`, `shutil`)

## Project Structure

```
GeekBrains-Python-Immersion/
├── Lesson_1/
│   ├── task_1_triangle.py
│   ├── task_2_prime_number.py
│   └── task_3_guess_number.py
├── Lesson_2/
│   ├── task_1_int_to_hex.py
│   └── task_2_fraction_operations.py
├── Lesson_3/
│   ├── task_1_list_duplicates.py
│   ├── task_2_frequent_words.py
│   └── task_3_backpack_problem.py
├── Lesson_4/
│   ├── task_1_keyword_args_to_dict.py
│   └── task_2_atm_refactored.py
├── Lesson_5/
│   ├── task_1_parse_filepath.py
│   ├── task_2_dict_generator.py
│   └── task_3_fibonacci_generator.py
├── Lesson_6/
│   ├── task_1_date_validator.py
│   └── chess_package/
│       ├── __init__.py
│       └── task_2_and_3_eight_queens.py
├── Lesson_7/
│   ├── task_1_batch_rename.py
│   └── file_management_package/
│       ├── __init__.py
│       ├── renaming.py
│       └── parsing.py
├── .gitignore
└── README.md
```

## Lesson Summaries

### Lesson 1: Introduction to Python Basics
*   [`task_1_triangle.py`](Lesson_1/task_1_triangle.py): Checks if a triangle can be formed from three side lengths and determines its type (equilateral, isosceles, or scalene).
*   [`task_2_prime_number.py`](Lesson_1/task_2_prime_number.py): Checks if a number (between 0 and 100,000) is prime or composite.
*   [`task_3_guess_number.py`](Lesson_1/task_3_guess_number.py): A game where the user guesses a number between 0 and 1000 in 10 attempts.

### Lesson 2: Basic Data Types and Operations
*   [`task_1_int_to_hex.py`](Lesson_2/task_1_int_to_hex.py): Converts an integer to its hexadecimal string representation, with a check against the built-in `hex()` function.
*   [`task_2_fraction_operations.py`](Lesson_2/task_2_fraction_operations.py): Accepts two fractions as strings ("a/b"), calculates their sum and product using a custom `Fraction` class, and verifies against Python's `fractions` module.

### Lesson 3: Collections and Data Structures
*   [`task_1_list_duplicates.py`](Lesson_3/task_1_list_duplicates.py): Finds and returns unique duplicate elements from a list.
*   [`task_2_frequent_words.py`](Lesson_3/task_2_frequent_words.py): Counts word frequencies in a given text (ignoring punctuation and case) and returns the top 10 most frequent words using a `TextAnalyzer` class.
*   [`task_3_backpack_problem.py`](Lesson_3/task_3_backpack_problem.py): Solves the backpack problem. Given a dictionary of items and their weights, and a maximum backpack capacity, it finds all possible combinations of items that fit, using a `BackpackProblemSolver` class.

### Lesson 4: Functions and Program Flow
*   [`task_1_keyword_args_to_dict.py`](Lesson_4/task_1_keyword_args_to_dict.py): A function (within `KwargsProcessor` class) that accepts keyword arguments and returns a dictionary where keys are argument values (or their string representation if unhashable) and values are argument names.
*   [`task_2_atm_refactored.py`](Lesson_4/task_2_atm_refactored.py): An ATM program refactored into an `ATM` class. It handles deposits, withdrawals (with fees and multiple-of-50 rule), interest accrual, and wealth tax. All operations are logged.

### Lesson 5: Modules and Packages
*   [`task_1_parse_filepath.py`](Lesson_5/task_1_parse_filepath.py): A function (within `FilePathParser` class) that takes an absolute file path string and returns a tuple: (path, filename, extension).
*   [`task_2_dict_generator.py`](Lesson_5/task_2_dict_generator.py): A one-line dictionary generator (within a `SalaryCalculator` class method) that takes three lists (names, rates, bonus percentages) and returns a dictionary of names to calculated bonus amounts.
*   [`task_3_fibonacci_generator.py`](Lesson_5/task_3_fibonacci_generator.py): A generator function (within `FibonacciGenerator` class) for Fibonacci numbers.

### Lesson 6: Advanced Topics - Date/Time and Problem Solving
*   [`task_1_date_validator.py`](Lesson_6/task_1_date_validator.py): A module with a `DateValidator` class to check if a date string is valid (including leap year logic). Runnable from the terminal.
*   `chess_package/`: A package for chess-related problems.
    *   [`task_2_and_3_eight_queens.py`](Lesson_6/chess_package/task_2_and_3_eight_queens.py): Contains an `EightQueensSolver` class.
        *   Task 2: `are_queens_safe(positions)`: Checks if 8 queens on a chessboard are attacking each other.
        *   Task 3: `find_four_safe_random_placements()`: Finds and prints 4 unique successful random placements of 8 queens.

### Lesson 7: File Operations and System Interaction
*   [`task_1_batch_rename.py`](Lesson_7/task_1_batch_rename.py): A script demonstrating the use of the `BatchFileRenamer` from the `file_management_package` for group renaming of files.
*   `file_management_package/`: A package for file management utilities.
    *   `__init__.py`: Exposes `FilePathParser` and `BatchFileRenamer`.
    *   [`renaming.py`](Lesson_7/file_management_package/renaming.py): Contains the `BatchFileRenamer` class for batch renaming of files with various criteria.
    *   [`parsing.py`](Lesson_7/file_management_package/parsing.py): Contains the `FilePathParser` class (originally from Lesson 5) for parsing file paths.

---
This README provides a general overview. For detailed information on each task, please refer to the source code and comments within the respective Python files.

## Contact
Artyom (DeOcxan)  
"DeOcxan" = Decentralized Ocean of innovation, reflecting my focus on ML & Blockchain  
For inquiries, see my GitHub profile: github.com/DeOcxan

## Last Updated
May 18, 2025

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
