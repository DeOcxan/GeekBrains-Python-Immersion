import os
from typing import Optional, Tuple, List

class BatchFileRenamer:
    """Provides functionality to batch rename files in a directory."""

    def __init__(self):
        pass

    def rename_files(
        self,
        directory: str,
        source_extension: str,
        target_extension: str,
        num_digits: int = 3,
        desired_final_name: Optional[str] = None,
        original_name_slice: Optional[Tuple[int, int]] = None,
    ) -> List[Tuple[str, str]]:
        """
        Renames files in a specified directory based on given criteria.

        Args:
            directory: The path to the directory containing files to rename.
            source_extension: The original extension of files to rename (".txt").
                              Must include the leading dot.
            target_extension: The new extension for the renamed files (".log").
                              Must include the leading dot.
            num_digits: The number of digits for the sequential counter (3 for 001, 002).
            desired_final_name: The desired base name for the new files. If None, this part is omitted.
            original_name_slice: A tuple (start, end) for 1-based inclusive slicing of the
                                 original filename (excluding extension) to be preserved.
                                 , (3, 6) takes characters from 3rd to 6th.
                                 If None, no part of the original name is preserved this way.
        
        Returns:
            A list of tuples, where each tuple is (old_path, new_path) for successfully renamed files.
        
        Raises:
            FileNotFoundError: If the specified directory does not exist.
            ValueError: For invalid parameters (num_digits <= 0).
            TypeError: For incorrect parameter types.
        """

        # Parameter Validation
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")
        if not isinstance(source_extension, str) or not source_extension.startswith('.'):
            raise ValueError("source_extension must be a string starting with '.' ('.txt')")
        if not isinstance(target_extension, str) or not target_extension.startswith('.'):
            raise ValueError("target_extension must be a string starting with '.' ('.log')")
        if not isinstance(num_digits, int) or num_digits <= 0:
            raise ValueError("num_digits must be a positive integer.")
        if desired_final_name is not None and not isinstance(desired_final_name, str):
            raise TypeError("desired_final_name must be a string or None.")
        if original_name_slice is not None:
            if not (isinstance(original_name_slice, tuple) and len(original_name_slice) == 2 and
                    isinstance(original_name_slice[0], int) and isinstance(original_name_slice[1], int) and
                    0 < original_name_slice[0] <= original_name_slice[1]):
                raise ValueError("original_name_slice must be a tuple of two positive integers (start, end) with start <= end.")

        renamed_files_log: List[Tuple[str, str]] = []
        counter = 1

        try:
            files_in_directory = sorted(os.listdir(directory))
        except OSError as e:
            print(f"Error listing directory {directory}: {e}")
            return renamed_files_log

        for filename_full in files_in_directory:
            original_filepath = os.path.join(directory, filename_full)

            if not os.path.isfile(original_filepath):
                continue

            original_name_part, current_extension = os.path.splitext(filename_full)

            if current_extension.lower() == source_extension.lower():
                name_slice_component = ""
                if original_name_slice and original_name_part:
                    start_index = original_name_slice[0] - 1 
                    end_index = original_name_slice[1]
                    if 0 <= start_index < len(original_name_part) and start_index < end_index:
                        name_slice_component = original_name_part[start_index:end_index]
                
                desired_name_component = desired_final_name if desired_final_name else ""
                counter_str = str(counter).zfill(num_digits)
                
                new_name_parts = []
                if name_slice_component:
                    new_name_parts.append(name_slice_component)
                if desired_name_component:
                    new_name_parts.append(desired_name_component)
                new_name_parts.append(counter_str)
                
                new_filename_base = "_".join(filter(None, new_name_parts))
                if not new_filename_base:
                    new_filename_base = f"file_{counter_str}"

                new_filename_full = new_filename_base + target_extension
                new_filepath = os.path.join(directory, new_filename_full)

                if os.path.exists(new_filepath):
                    print(f"Warning: File '{new_filepath}' already exists. Skipping rename of '{filename_full}'.")
                    continue

                try:
                    os.rename(original_filepath, new_filepath)
                    # print(f"Renamed: '{original_filepath}' -> '{new_filepath}'") # Optional: keep for module use
                    renamed_files_log.append((original_filepath, new_filepath))
                    counter += 1
                except OSError as e:
                    print(f"Error renaming file '{original_filepath}' to '{new_filepath}': {e}")
        
        return renamed_files_log 