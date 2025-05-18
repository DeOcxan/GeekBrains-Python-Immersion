from typing import List, TypeVar, Hashable

T = TypeVar('T', bound=Hashable) # Ensure elements are hashable for set operations

def find_duplicates(data: List[T]) -> List[T]:
    """
    Given a list of elements, returns a list containing only the elements
    that appear more than once in the input list.
    The resulting list of duplicates will not contain duplicates itself.

    Args:
        data: A list of hashable elements.

    Returns:
        A list of unique elements that were duplicated in the input list.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(item, Hashable) for item in data):
        # This check is more for type hinting satisfaction, actual hashability errors
        # would occur during set/dict operations if an item is not hashable.
        raise TypeError("All items in the list must be hashable.")

    seen = set()
    duplicates_set = set()

    for item in data:
        if item in seen:
            duplicates_set.add(item)
        else:
            seen.add(item)
    
    return list(duplicates_set)

def main():
    """
    Main function to demonstrate the find_duplicates function.
    """
    sample_list1 = [1, 2, 2, 3, 4, 4, 4, 5, "hello", "world", "hello"]
    print(f"Original list: {sample_list1}")
    duplicates1 = find_duplicates(sample_list1)
    print(f"Duplicate elements: {duplicates1}")

    sample_list2 = [10, 20, 30, 40, 50] # No duplicates
    print(f"\nOriginal list: {sample_list2}")
    duplicates2 = find_duplicates(sample_list2)
    print(f"Duplicate elements: {duplicates2}")

    sample_list3 = ["a", "b", "a", "c", "b", "a", "d", "a"]
    print(f"\nOriginal list: {sample_list3}")
    duplicates3 = find_duplicates(sample_list3)
    print(f"Duplicate elements: {duplicates3}")

    sample_list4 = [] # Empty list
    print(f"\nOriginal list: {sample_list4}")
    duplicates4 = find_duplicates(sample_list4)
    print(f"Duplicate elements: {duplicates4}")

    # Example with non-hashable (will fail if not caught, but TypeVar helps hint)
    # try:
    #     sample_list_error = [1, 2, [3, 4], 2, [3, 4]]
    #     print(f"\nOriginal list: {sample_list_error}")
    #     duplicates_error = find_duplicates(sample_list_error)
    #     print(f"Duplicate elements: {duplicates_error}")
    # except TypeError as e:
    #     print(f"Error with non-hashable list: {e}")

if __name__ == "__main__":
    main() 