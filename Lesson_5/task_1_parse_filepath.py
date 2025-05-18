import os
from typing import Tuple

class FilePathParser:
    """Parses an absolute file path into its components."""

    def __init__(self):
        pass

    def parse_path(self, absolute_path: str) -> Tuple[str, str, str]:
        """
        Takes an absolute file path string and returns a tuple containing:
        (path, file_name, file_extension)

        Args:
            absolute_path: The absolute path to the file.

        Returns:
            A tuple (path_to_file, file_name_only, file_extension_only).
            Returns (absolute_path, "", "") if path is a directory or does not have an extension.
        """
        if not isinstance(absolute_path, str):
            raise TypeError("Input path must be a string.")
        if not absolute_path.strip():
            raise ValueError("Input path cannot be empty or just whitespace.")
        # It's good practice to normalize the path, especially if dealing with mixed separators
        normalized_path = os.path.normpath(absolute_path)

        # Get the directory part of the path
        path_to_file = os.path.dirname(normalized_path)
        
        # Get the full file name (including extension)
        full_file_name = os.path.basename(normalized_path)
        
        # Split the full file name into name and extension
        # os.path.splitext splits 'file.ext' into ('file', '.ext')
        # or ('file', '') if no extension, or ('.bashrc', '') if it's like a dotfile
        file_name_only, file_extension_only = os.path.splitext(full_file_name)
        
        # Handle cases like ".bashrc" where splitext might return (".bashrc", "")
        # If file_name_only starts with a dot and has no extension, then it is the filename.
        # However, the standard behavior of splitext is usually what's desired.
        # For example, for "/path/to/.config", basename is ".config", splitext is (".config", "")
        # For "/path/to/archive.tar.gz", basename is "archive.tar.gz", splitext is ("archive.tar", ".gz")
        # The current split handles common cases well.

        return path_to_file, file_name_only, file_extension_only

def main():
    """
    Main function to demonstrate the FilePathParser.
    """
    parser = FilePathParser()

    test_paths = [
        "/Users/username/Documents/MyProject/src/main.py",
        "C:\\Program Files\\MyApp\\app.exe",
        "/usr/local/bin/scriptfile", # No extension
        "/home/user/.bashrc",          # Dotfile, often considered no extension by splitext
        "archive.tar.gz",              # Relative path, but os.path functions handle it
        "/var/log/sys.log.1",
        "C:/Windows/System32/drivers/etc/hosts", # Mixed slashes
        "/data/files/image.JPEG",
        "/directory/only/",            # A directory path
    ]

    for i, path_str in enumerate(test_paths):
        print(f"--- Case {i+1} ---")
        print(f"Original path: {path_str}")
        try:
            path_tuple = parser.parse_path(path_str)
            print(f"Parsed tuple: (Path: '{path_tuple[0]}', Name: '{path_tuple[1]}', Extension: '{path_tuple[2]}')\n")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}\n")

    # Test with invalid input
    print("--- Case: Invalid Input (integer) ---")
    try:
        parser.parse_path(12345) # type: ignore
    except TypeError as e:
        print(f"Error: {e}\n")

    print("--- Case: Invalid Input (empty string) ---")
    try:
        parser.parse_path("  ")
    except ValueError as e:
        print(f"Error: {e}\n")

if __name__ == "__main__":
    main() 