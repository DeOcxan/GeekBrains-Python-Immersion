"""
Lesson 8, Task 1: Directory Traversal and Serialization (Example Usage)

This script demonstrates the use of the DirectoryScanner class from the
file_processing_suite package to scan a directory and save its structure.
"""
import os
import argparse
import shutil

# Import from the new package
# Assuming the script is run from the root of GeekBrains-Python-Immersion or Lesson_8 is in PYTHONPATH
# For robust execution, ensure correct PYTHONPATH or use relative imports if task_1 is moved into a package itself.
# Let's try a relative import assuming execution from Lesson_8 directory or if this script itself becomes part of a package later.
# from .file_processing_suite import DirectoryScanner # This would be if task_1 was a module in a package

# For direct script execution from project root or Lesson_8, we might need to adjust Python path
# or use a more direct import if the structure allows. Let's assume standard package discovery.
try:
    from file_processing_suite.directory_scanner import DirectoryScanner
except ImportError:
    # Fallback for simpler execution context or if path issues arise, e.g. when running script directly from Lesson_8
    # This assumes that file_processing_suite is in the same directory or Python's search path.
    # For a real package, you'd install it or set PYTHONPATH.
    # A common way if running from parent of Lesson_8:
    # from Lesson_8.file_processing_suite.directory_scanner import DirectoryScanner
    print("Attempting import with adjusted path for DirectoryScanner...")
    import sys
    # Assuming script is in Lesson_8 and package is Lesson_8/file_processing_suite
    # Add parent of Lesson_8 to path to allow `from Lesson_8.file_processing_suite...`
    package_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if package_parent_dir not in sys.path:
        sys.path.insert(0, package_parent_dir)
    from Lesson_8.file_processing_suite.directory_scanner import DirectoryScanner


# The DirectoryEntry TypedDict is defined in directory_scanner module and implicitly used by DirectoryScanner.
# No need to redefine it here if only DirectoryScanner is used directly.

def _create_dummy_dir_for_testing(base_dir_name: str = "test_scan_dir") -> str:
    """Creates a dummy directory structure for testing the scanner. Returns the path."""
    current_working_dir = os.getcwd()
    base_path = os.path.join(current_working_dir, base_dir_name)

    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(os.path.join(base_path, "subdir1"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "subdir2", "subsubdir"), exist_ok=True)

    with open(os.path.join(base_path, "file1.txt"), "w") as f:
        f.write("This is file1 in root test dir.") # 30 bytes
    with open(os.path.join(base_path, "subdir1", "file2.log"), "w") as f:
        f.write("This is file2 in subdir1.") # 26 bytes
    with open(os.path.join(base_path, "subdir2", "file3.dat"), "w") as f:
        f.write("This is file3 in subdir2.") # 26 bytes
    with open(os.path.join(base_path, "subdir2", "subsubdir", "file4.ini"), "w") as f:
        f.write("Tiny") # 4 bytes
    
    print(f"Created dummy directory at: {base_path}")
    return base_path

def _cleanup_dummy_dir(dir_path: str):
    """Cleans up the dummy directory."""
    # Safety check: only remove if it's the known dummy directory name and path seems correct
    if os.path.exists(dir_path) and os.path.basename(dir_path) == "test_scan_dir": 
        try:
            shutil.rmtree(dir_path)
            print(f"Cleaned up dummy directory: {dir_path}")
        except Exception as e:
            print(f"Error cleaning up dummy directory {dir_path}: {e}")
    else:
        print(f"Cleanup skipped: Path {dir_path} does not exist or is not the expected test directory name.")

def main():
    """Main function to handle argument parsing and initiate directory scan using the package."""
    parser = argparse.ArgumentParser(
        description="Scan a directory using DirectoryScanner from file_processing_suite and save its structure."
    )
    parser.add_argument(
        "input_dir", 
        nargs='?', 
        type=str, 
        help="The directory to scan. (Required if --test_dummy is not set)"
    )
    parser.add_argument(
        "--output_dir", 
        type=str, 
        default="scan_results", 
        help="The directory where JSON, CSV, and Pickle files will be saved. (Default: scan_results)"
    )
    parser.add_argument(
        "--test_dummy",
        action="store_true",
        help="If set, creates 'test_scan_dir', scans it, places results in 'test_scan_dir_results', and then cleans up 'test_scan_dir'."
    )

    args = parser.parse_args()

    input_directory_to_scan = args.input_dir
    output_directory_for_results = args.output_dir
    dummy_dir_path_for_cleanup = None

    if args.test_dummy:
        print("Running with test dummy directory...")
        dummy_dir_name = "test_scan_dir"
        input_directory_to_scan = _create_dummy_dir_for_testing(dummy_dir_name)
        dummy_dir_path_for_cleanup = input_directory_to_scan
        output_directory_for_results = os.path.join(os.getcwd(), "test_scan_dir_results")
        print(f"Test scan results will be saved to: {output_directory_for_results}")
    elif not input_directory_to_scan:
        parser.error("The following arguments are required: input_dir (unless --test_dummy is used)")
        return # Should exit due to parser.error

    if not os.path.isdir(input_directory_to_scan):
        print(f"Error: Input directory '{input_directory_to_scan}' not found or is not a directory.")
        if not args.test_dummy: # If not test_dummy, it's a user error
             parser.print_help()
        return

    try:
        # Use the DirectoryScanner from the package
        scanner = DirectoryScanner(input_directory_to_scan)
        
        # The scan_directory method is called lazily by get_collected_data or explicitly.
        # Let's call it explicitly to make sure data is generated before accessing it.
        scan_data = scanner.scan_directory()

        if not scan_data:
            print(f"No items found in directory '{input_directory_to_scan}' or directory is empty.")
            return

        os.makedirs(output_directory_for_results, exist_ok=True)

        scanned_dir_name = os.path.basename(os.path.normpath(input_directory_to_scan))
        if scanned_dir_name == '.' or not scanned_dir_name: # Handle cases like '.' or './'
            scanned_dir_name = "current_directory"
        
        base_output_filename = f"{scanned_dir_name}_scan"

        json_path = os.path.join(output_directory_for_results, f"{base_output_filename}.json")
        csv_path = os.path.join(output_directory_for_results, f"{base_output_filename}.csv")
        pickle_path = os.path.join(output_directory_for_results, f"{base_output_filename}.pkl")

        scanner.save_to_json(json_path) # save_to_json will call get_collected_data if needed
        scanner.save_to_csv(csv_path)
        scanner.save_to_pickle(pickle_path)

        print(f"\nScan complete. Results saved in '{output_directory_for_results}'.")
        
        # Optional: Print some data for quick verification
        # print("\nSample of Collected Data (first 3 entries):")
        # for item in scan_data[:3]:
        #     print(item)

    except ValueError as ve:
        print(f"Configuration Error: {ve}")
    except ImportError as ie:
        print(f"Import Error: {ie}. Ensure the file_processing_suite package is correctly placed and discoverable.")
        print("If running from the project root, try: python Lesson_8/task_1_directory_serializer.py ...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        if args.test_dummy and dummy_dir_path_for_cleanup:
            # Prompt before cleanup, or make cleanup optional via another flag
            # For now, let's keep auto-cleanup for the dummy test.
            _cleanup_dummy_dir(dummy_dir_path_for_cleanup)


if __name__ == "__main__":
    # To run this script, ensure that the GeekBrains-Python-Immersion directory (parent of Lesson_8)
    # is in your PYTHONPATH, or run the script from that root directory, e.g.:
    # python Lesson_8/task_1_directory_serializer.py --test_dummy
    # python Lesson_8/task_1_directory_serializer.py . --output_dir "scan_of_current_dir"
    # python Lesson_8/task_1_directory_serializer.py ../Lesson_7 --output_dir "scan_of_lesson7"

    main() 