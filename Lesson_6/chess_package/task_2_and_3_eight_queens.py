import random
from typing import List, Tuple, Set

class EightQueensSolver:
    """Solves and verifies solutions for the 8 Queens puzzle."""

    _BOARD_SIZE = 8

    def __init__(self):
        pass # No state needed for these static-like methods

    def are_queens_safe(self, positions: List[Tuple[int, int]]) -> bool:
        """
        Checks if a given list of queen positions is safe (no two queens attack each other).
        Positions are 1-indexed (row, col) from 1 to 8.

        Args:
            positions: A list of 8 tuples, where each tuple is (row, col).

        Returns:
            True if no two queens attack each other, False otherwise.
        """
        if not isinstance(positions, list) or len(positions) != self._BOARD_SIZE:
            # For the specific problem, we expect 8 queens.
            # If checking a general N-queens, len(positions) would be N.
            print(f"Error: Expected a list of {self._BOARD_SIZE} queen positions.")
            return False # Or raise ValueError

        if not all(isinstance(pos, tuple) and len(pos) == 2 for pos in positions):
            print("Error: Each position must be a tuple of (row, col).")
            return False

        if not all(isinstance(r, int) and isinstance(c, int) and 
                   1 <= r <= self._BOARD_SIZE and 1 <= c <= self._BOARD_SIZE 
                   for r, c in positions):
            print(f"Error: Coordinates must be integers between 1 and {self._BOARD_SIZE}.")
            return False

        # Check for duplicate positions (two queens in the same spot)
        if len(set(positions)) != len(positions):
            print("Error: Duplicate queen positions found.")
            return False

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                # Check if they are in the same row
                if r1 == r2:
                    return False
                # Check if they are in the same column
                if c1 == c2:
                    return False
                # Check if they are in the same diagonal
                if abs(r1 - r2) == abs(c1 - c2):
                    return False
        return True

    def _generate_one_random_full_placement(self) -> List[Tuple[int, int]]:
        """
        Generates a random placement of 8 queens, one per column, to simplify generation.
        This means rows will be unique for each queen if placed one per column initially.
        Then we can check for diagonal attacks.
        A more naive approach would be to pick 8 random (row, col) pairs, but that has
        a higher chance of immediate row/col collisions and duplicate spots.
        
        This method ensures each queen is in a unique column.
        Rows are randomly assigned for each column.
        """
        positions: List[Tuple[int, int]] = []
        # Ensure one queen per column, rows are random
        rows = list(range(1, self._BOARD_SIZE + 1))
        random.shuffle(rows)
        for col_idx in range(self._BOARD_SIZE):
            # col is col_idx + 1 (1-indexed)
            # row is a shuffled row number
            positions.append((rows[col_idx], col_idx + 1))
        return positions
    
    def _generate_truly_random_placement(self) -> List[Tuple[int, int]]:
        """
        Generates 8 unique random (row, col) positions.
        This is more general but might take longer to find a safe placement.
        """
        possible_coords = [(r, c) for r in range(1, self._BOARD_SIZE + 1) for c in range(1, self._BOARD_SIZE + 1)]
        if len(possible_coords) < self._BOARD_SIZE:
             raise ValueError("Board size too small for the number of queens.") # Should not happen for 8x8
        return random.sample(possible_coords, self._BOARD_SIZE)


    def find_four_safe_random_placements(self, use_optimized_generation: bool = True) -> List[List[Tuple[int, int]]]:
        """
        Finds 4 successful random placements of 8 queens that do not attack each other.

        Args:
            use_optimized_generation: If True, uses a generation strategy where each queen
                                      is initially placed in a unique column. If False,
                                      uses a purely random (row,col) selection for each queen.
                                      Optimized is much faster.

        Returns:
            A list containing 4 lists of safe queen positions.
        """
        successful_placements: List[List[Tuple[int, int]]] = []
        attempts = 0
        max_attempts = 1_000_000 # Safety break for potentially very long searches with non-optimized

        while len(successful_placements) < 4 and attempts < max_attempts:
            if use_optimized_generation:
                random_positions = self._generate_one_random_full_placement()
            else:
                random_positions = self._generate_truly_random_placement()
            
            if self.are_queens_safe(random_positions):
                # Ensure we don't add the same solution if found multiple times by chance
                # Sorting makes the list of tuples canonical for set comparison
                sorted_pos = sorted(random_positions)
                is_new_solution = True
                for existing_solution in successful_placements:
                    if sorted(existing_solution) == sorted_pos:
                        is_new_solution = False
                        break
                if is_new_solution:
                    successful_placements.append(random_positions)
            attempts += 1
        
        if len(successful_placements) < 4:
            print(f"Warning: Could only find {len(successful_placements)} unique safe placements after {attempts} attempts.")
        
        return successful_placements

def main():
    """
    Main function to demonstrate the EightQueensSolver.
    """
    solver = EightQueensSolver()

    # Task 2: Check a given configuration
    print("--- Task 2: Checking specific queen placements ---")
    # Example of a known safe configuration (can be used for testing are_queens_safe)
    # This is one of the 92 solutions. (1-indexed)
    safe_config_1 = [(1, 4), (2, 6), (3, 8), (4, 2), (5, 7), (6, 1), (7, 3), (8, 5)]
    print(f"Checking safe_config_1: {safe_config_1}")
    is_safe = solver.are_queens_safe(safe_config_1)
    print(f"Are queens in safe_config_1 safe? {is_safe} (Expected: True)\n")

    # Example of a configuration with attacking queens
    unsafe_config_1 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)] # Diagonal attack
    print(f"Checking unsafe_config_1 (diagonal): {unsafe_config_1}")
    is_safe = solver.are_queens_safe(unsafe_config_1)
    print(f"Are queens in unsafe_config_1 safe? {is_safe} (Expected: False)\n")

    unsafe_config_2 = [(1, 1), (1, 8), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (2,5)] # Row attack
    print(f"Checking unsafe_config_2 (row): {unsafe_config_2}")
    is_safe = solver.are_queens_safe(unsafe_config_2)
    print(f"Are queens in unsafe_config_2 safe? {is_safe} (Expected: False)\n")
    
    unsafe_config_3 = [(1, 1), (8, 1), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (2,5)] # Column attack
    print(f"Checking unsafe_config_3 (column): {unsafe_config_3}")
    is_safe = solver.are_queens_safe(unsafe_config_3)
    print(f"Are queens in unsafe_config_3 safe? {is_safe} (Expected: False)\n")

    # Example of an invalid input (not 8 queens)
    invalid_config_1 = [(1,1), (2,3)]
    print(f"Checking invalid_config_1 (not 8 queens): {invalid_config_1}")
    # This will print an error and return False due to the check inside are_queens_safe
    is_safe = solver.are_queens_safe(invalid_config_1)
    print(f"Are queens in invalid_config_1 safe? {is_safe} (Expected: False or error message from function)\n")

    # Task 3: Find and print 4 successful random placements
    print("--- Task 3: Finding 4 successful random placements (optimized generation) ---")
    # Using the optimized generation (one queen per column then check diagonals)
    # This is much more efficient for finding solutions to N-Queens.
    successful_placements = solver.find_four_safe_random_placements(use_optimized_generation=True)
    if successful_placements:
        print(f"Found {len(successful_placements)} successful random placements:")
        for i, placement in enumerate(successful_placements):
            # Sort for consistent display if needed, but raw placement is fine
            print(f"  Placement {i+1}: {sorted(placement)}") 
    else:
        print("Could not find 4 successful placements with optimized generation within limits.")
    print("\n")

    # Optional: Demonstrate with purely random (less efficient)
    # print("--- Task 3: Finding 4 successful random placements (purely random generation) ---")
    # print("(This might take a noticeable amount of time)")
    # successful_placements_pure_random = solver.find_four_safe_random_placements(use_optimized_generation=False)
    # if successful_placements_pure_random:
    #     print(f"Found {len(successful_placements_pure_random)} successful_placements_pure_random placements:")
    #     for i, placement in enumerate(successful_placements_pure_random):
    #         print(f"  Placement {i+1}: {sorted(placement)}")
    # else:
    #     print("Could not find 4 successful placements with purely random generation within limits.")

if __name__ == "__main__":
    # This allows running the demos when the script is executed directly.
    # To use the solver from another script:
    # from chess_package.task_2_and_3_eight_queens import EightQueensSolver
    # solver = EightQueensSolver()
    # result = solver.are_queens_safe([(1,1), ...])
    main() 