from typing import Dict, List, Tuple, Any, Set
import itertools

class BackpackProblemSolver:
    """Solves the backpack problem to find all combinations of items that fit."""

    def __init__(self, items: Dict[str, float], max_weight: float):
        if not isinstance(items, dict):
            raise TypeError("Items must be a dictionary.")
        if not all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in items.items()):
            raise ValueError("Item keys must be strings and values must be numbers (weights).")
        if not isinstance(max_weight, (int, float)) or max_weight < 0:
            raise ValueError("Max weight must be a non-negative number.")
        
        self._items = items
        self._item_names = list(items.keys()) # Keep a consistent order for combinations
        self._max_weight = max_weight

    def get_valid_combinations(self) -> List[List[str]]:
        """
        Finds all combinations of items whose total weight does not exceed max_weight.

        Returns:
            A list of lists, where each inner list is a valid combination of item names.
        """
        all_valid_combinations: List[List[str]] = [] # Explicitly type the list

        num_items = len(self._item_names)

        # Iterate through all possible numbers of items to pick (from 1 to num_items)
        for r in range(1, num_items + 1):
            # Generate all combinations of size r
            for current_combination_tuple in itertools.combinations(self._item_names, r):
                current_combination_list = list(current_combination_tuple)
                current_weight = sum(self._items[item_name] for item_name in current_combination_list)
                
                if current_weight <= self._max_weight:
                    all_valid_combinations.append(current_combination_list)
        
        return all_valid_combinations

    @property
    def items(self) -> Dict[str, float]:
        return self._items

    @property
    def max_weight(self) -> float:
        return self._max_weight

def main():
    """
    Main function to demonstrate the BackpackProblemSolver.
    """
    items_for_hike = {
        "tent": 3.5,
        "sleeping_bag": 1.5,
        "water_filter": 0.5,
        "food_pack": 2.0,
        "cooking_pot": 0.8,
        "first_aid_kit": 0.7,
        "rain_jacket": 0.4,
        "headlamp": 0.1
    }
    backpack_capacity = 5.0

    print(f"Items available: {items_for_hike}")
    print(f"Backpack capacity: {backpack_capacity} kg\n")

    try:
        solver = BackpackProblemSolver(items_for_hike, backpack_capacity)
        valid_kits = solver.get_valid_combinations()

        if not valid_kits:
            print("No combination of items fits into the backpack with the given capacity.")
        else:
            print(f"Found {len(valid_kits)} possible combinations of items that fit:")
            for i, kit in enumerate(valid_kits):
                kit_weight = sum(solver.items[item] for item in kit)
                print(f"  Combination {i+1}: {kit} (Total weight: {kit_weight:.2f} kg)")
        
        # Example with a very small capacity
        print("\n--- Example with smaller capacity (1.0 kg) ---")
        small_capacity_solver = BackpackProblemSolver(items_for_hike, 1.0)
        small_valid_kits = small_capacity_solver.get_valid_combinations()
        if not small_valid_kits:
            print("No combination of items fits into the backpack with 1.0 kg capacity.")
        else:
            print(f"Found {len(small_valid_kits)} possible combinations for 1.0 kg capacity:")
            for i, kit in enumerate(small_valid_kits):
                kit_weight = sum(small_capacity_solver.items[item] for item in kit)
                print(f"  Combination {i+1}: {kit} (Total weight: {kit_weight:.2f} kg)")


    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
