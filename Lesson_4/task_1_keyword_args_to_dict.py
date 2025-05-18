from typing import Dict, Any, Hashable

class KwargsProcessor:
    """Processes keyword arguments to create a specific dictionary output."""

    def __init__(self):
        pass

    def process_kwargs_to_dict(self, **kwargs: Any) -> Dict[Any, str]:
        """
        Accepts only keyword parameters and returns a dictionary where the key is
        the value of the passed argument, and the value is the name of the argument.
        If a key (argument value) is not hashable, its string representation is used.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A dictionary where keys are argument values (or their string representations)
            and values are argument names.
        """
        result_dict: Dict[Any, str] = {}
        for arg_name, arg_value in kwargs.items():
            key_to_use: Any
            try:
                # Attempt to use the value as a key directly
                # This requires the value to be hashable
                hash(arg_value)
                key_to_use = arg_value
            except TypeError: # If arg_value is not hashable
                key_to_use = str(arg_value)
            
            # Handle potential key collisions if different unhashable items stringify to the same value,
            # or if a hashable value equals the string representation of another.
            # For this task, the requirement is to use the string representation, so if multiple
            # original values map to the same key, the last one processed will overwrite previous ones.
            # If distinct handling for collisions is needed, the logic would be more complex.
            result_dict[key_to_use] = arg_name
        return result_dict

def main():
    """
    Main function to demonstrate the KwargsProcessor.
    """
    processor = KwargsProcessor()

    # Case 1: Basic hashable types
    print("--- Case 1: Basic Hashable Types ---")
    result1 = processor.process_kwargs_to_dict(name="Alice", age=30, city="New York", active=True, score=98.5)
    print(f"kwargs: name=\"Alice\", age=30, city=\"New York\", active=True, score=98.5")
    print(f"Resulting dict: {result1}\n")

    # Case 2: Including an unhashable type (list)
    print("--- Case 2: Including an Unhashable Type (list) ---")
    hobbies_list = ["reading", "hiking"]
    result2 = processor.process_kwargs_to_dict(id=123, data=hobbies_list, status="pending")
    print(f"kwargs: id=123, data={hobbies_list}, status=\"pending\"")
    print(f"Resulting dict: {result2}\n")

    # Case 3: Including another unhashable type (dict)
    print("--- Case 3: Including an Unhashable Type (dict) ---")
    details_dict = {"country": "USA", "zip": "10001"}
    result3 = processor.process_kwargs_to_dict(user="Bob", info=details_dict, count=5)
    print(f"kwargs: user=\"Bob\", info={details_dict}, count=5")
    print(f"Resulting dict: {result3}\n")

    # Case 4: All unhashable types
    print("--- Case 4: All Unhashable Types ---")
    set_a = {1, 2}
    list_b = [3, 4]
    dict_c = {'x': 5}
    result4 = processor.process_kwargs_to_dict(param1=set_a, param2=list_b, param3=dict_c)
    print(f"kwargs: param1={set_a}, param2={list_b}, param3={dict_c}")
    print(f"Resulting dict: {result4}\n")

    # Case 5: Potential key collision after string conversion
    print("--- Case 5: Potential Key Collision after String Conversion ---")
    # Here, str([1,2]) will be '[1, 2]', and if another arg value is already the string '[1, 2]'
    # or another unhashable that stringifies to it, the latter will overwrite.
    result5 = processor.process_kwargs_to_dict(item_a=[1, 2], item_b="[1, 2]") 
    print(f"kwargs: item_a={[1, 2]}, item_b=\"[1, 2]\"")
    print(f"Resulting dict: {result5}\n")
    
    result5_ordered = processor.process_kwargs_to_dict(item_b="[1, 2]", item_a=[1, 2]) 
    print(f"kwargs: item_b=\"[1, 2]\", item_a={[1, 2]}")
    print(f"Resulting dict (order swapped): {result5_ordered}\n")

    # Case 6: Empty kwargs
    print("--- Case 6: Empty kwargs ---")
    result6 = processor.process_kwargs_to_dict()
    print(f"kwargs: (none)")
    print(f"Resulting dict: {result6}\n")

if __name__ == "__main__":
    main() 