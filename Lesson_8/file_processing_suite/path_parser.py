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
        file_name_only, file_extension_only = os.path.splitext(full_file_name)
        
        return path_to_file, file_name_only, file_extension_only

# Example usage can be removed or kept if this module is run directly for tests
# def main():
#     parser = FilePathParser()
#     test_paths = [
#         "/Users/username/Documents/MyProject/src/main.py",
#         "C:\\Program Files\\MyApp\\app.exe",
#         "/usr/local/bin/scriptfile",
#         "/home/user/.bashrc",
#         "archive.tar.gz"
#     ]
#     for path_str in test_paths:
#         print(f"Original path: {path_str}")
#         path_tuple = parser.parse_path(path_str)
#         print(f"Parsed tuple: (Path: '{path_tuple[0]}', Name: '{path_tuple[1]}', Extension: '{path_tuple[2]}')\n")

# if __name__ == "__main__":
#     main() 