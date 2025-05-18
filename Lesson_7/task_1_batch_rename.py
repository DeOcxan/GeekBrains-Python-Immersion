import os
import shutil
from typing import Optional, Tuple, List
from Lesson_7.file_management_package import BatchFileRenamer, FilePathParser

def _create_dummy_files(target_dir: str, files_to_create: List[str]):
    """Helper to create dummy files for testing."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for fname in files_to_create:
        with open(os.path.join(target_dir, fname), 'w') as f:
            f.write("dummy content for " + fname)

def _cleanup_dummy_files(target_dir: str, files_to_remove: Optional[List[str]] = None):
    """Helper to remove dummy files or the whole directory after testing."""
    if files_to_remove:
        for fname in files_to_remove:
            fpath = os.path.join(target_dir, fname)
            if os.path.exists(fpath):
                os.remove(fpath)
        # Optionally remove dir if empty, but for safety might leave it
        if not os.listdir(target_dir): 
            os.rmdir(target_dir)
        elif target_dir == "_temp_rename_test_dir": # a bit specific, but for safety
            print(f"Directory {target_dir} not empty, not removing it fully.")
    elif os.path.exists(target_dir) and target_dir == "_temp_rename_test_dir": # Safety: only remove this specific temp dir
        shutil.rmtree(target_dir)


def main_example():
    """Example usage of the BatchFileRenamer."""
    renamer = BatchFileRenamer()
    test_dir = "_temp_rename_test_dir" # Create a temporary directory for testing

    # --- Scenario 1 ---
    print("--- Scenario 1: Basic rename with desired name and counter ---")
    dummy_files_s1 = ["original_image_01.jpeg", "another_photo_alpha.jpeg", "IMG_12345.jpeg", "document.txt"]
    _create_dummy_files(test_dir, dummy_files_s1)
    try:
        renamed_s1 = renamer.rename_files(
            directory=test_dir,
            source_extension=".jpeg",
            target_extension=".jpg",
            num_digits=4,
            desired_final_name="vacation_pic"
        )
        print(f"Scenario 1 Renamed: {len(renamed_s1)} files.")
    except Exception as e:
        print(f"Error in Scenario 1: {e}")
    _cleanup_dummy_files(test_dir) # Clean up for next scenario
    print("\n")

    # --- Scenario 2 ---
    print("--- Scenario 2: Preserving original name slice ---")
    dummy_files_s2 = ["archive_file_jan.data", "archive_file_feb.data", "some_other_file.txt"]
    _create_dummy_files(test_dir, dummy_files_s2)
    try:
        renamed_s2 = renamer.rename_files(
            directory=test_dir,
            source_extension=".data",
            target_extension=".dat",
            num_digits=2,
            desired_final_name="backup",
            original_name_slice=(1, 7) # , "archive" from "archive_file_jan"
        )
        print(f"Scenario 2 Renamed: {len(renamed_s2)} files.")
    except Exception as e:
        print(f"Error in Scenario 2: {e}")
    _cleanup_dummy_files(test_dir)
    print("\n")

    # --- Scenario 3 ---
    print("--- Scenario 3: No desired name, only slice and counter ---")
    dummy_files_s3 = ["my_important_document_v1.doc", "another_document_final.doc", "my_doc.docx"]
    _create_dummy_files(test_dir, dummy_files_s3)
    try:
        renamed_s3 = renamer.rename_files(
            directory=test_dir,
            source_extension=".doc",
            target_extension=".txt",
            num_digits=3,
            original_name_slice=(4, 12) # , "important" from "my_important_document_v1"
        )
        print(f"Scenario 3 Renamed: {len(renamed_s3)} files.")
    except Exception as e:
        print(f"Error in Scenario 3: {e}")
    _cleanup_dummy_files(test_dir)
    print("\n")

    # --- Scenario 4 ---
    print("--- Scenario 4: Source extension not found ---")
    dummy_files_s4 = ["file1.png", "file2.gif"]
    _create_dummy_files(test_dir, dummy_files_s4)
    try:
        renamed_s4 = renamer.rename_files(
            directory=test_dir,
            source_extension=".jpg", # This extension does not exist in dummy files
            target_extension=".jpeg",
            desired_final_name="image"
        )
        print(f"Scenario 4 Renamed: {len(renamed_s4)} files. (Expected: 0)")
    except Exception as e:
        print(f"Error in Scenario 4: {e}")
    _cleanup_dummy_files(test_dir)
    print("\n")
    
    # --- Scenario 5 ---
    print("--- Scenario 5: Invalid slice (start > end, or out of bounds for some) ---")
    dummy_files_s5 = ["short.txt", "very_long_filename_example.txt"]
    _create_dummy_files(test_dir, dummy_files_s5)
    try:
        print("Attempting with slice (10, 3) - should raise ValueError during validation:")
        renamer.rename_files(
            directory=test_dir,
            source_extension=".txt",
            target_extension=".bak",
            original_name_slice=(10,3) # Invalid slice start > end
        )
    except ValueError as e:
        print(f"Caught expected error for invalid slice: {e}")
    # Slice (1, 100) on "short.txt" will result in empty name_slice_component for "short.txt"
    print("\nAttempting with slice (1, 100) - valid, but might be out of bounds for some names:")
    renamed_s5b = renamer.rename_files(
        directory=test_dir,
        source_extension=".txt",
        target_extension=".bak",
        desired_final_name="sliced",
        original_name_slice=(1,100)
    )
    print(f"Scenario 5b Renamed: {len(renamed_s5b)} files.")
    _cleanup_dummy_files(test_dir)
    print("\n")

    print("Note: Test scenarios create and delete files in a temporary '_temp_rename_test_dir' directory.")

if __name__ == "__main__":
    main_example()

# Initialize parser
parser = FilePathParser()
# Call parser.parse_path(...) 