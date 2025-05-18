"""
Lesson 8, Task 1: Directory Traversal and Serialization (Core Logic)

This module contains the DirectoryScanner class and DirectoryEntry type definition.
"""
import os
import json
import csv
import pickle
from typing import List, TypedDict, Literal

class DirectoryEntry(TypedDict):
    """Structure for storing information about a directory item."""
    name: str
    path: str  # Relative path from the root_dir
    parent_directory: str # Relative path of the parent from root_dir, or special value for root's parent
    type: Literal["file", "directory"]
    size_bytes: int

class DirectoryScanner:
    """Scans a directory and saves its structure to various file formats."""

    def __init__(self, root_dir: str):
        if not os.path.isdir(root_dir):
            raise ValueError(f"Provided root directory '{root_dir}' does not exist or is not a directory.")
        self._root_dir = os.path.abspath(root_dir)
        self._collected_data: List[DirectoryEntry] = []

    def _get_directory_size(self, dir_path: str) -> int:
        """Calculates the total size of all files within a directory (recursively)."""
        total_size = 0
        for path, _, filenames in os.walk(dir_path):
            for f in filenames:
                fp = os.path.join(path, f)
                if not os.path.islink(fp):
                    try:
                        total_size += os.path.getsize(fp)
                    except FileNotFoundError:
                        print(f"Warning: File not found during size calculation: {fp}")
                        continue
        return total_size

    def scan_directory(self) -> List[DirectoryEntry]:
        """
        Recursively scans the root directory and collects information
        about all files and subdirectories.
        The root directory itself is the first entry in the list.
        """
        self._collected_data = []
        
        root_name = os.path.basename(self._root_dir)
        # Determine the parent of the root. For display, this could be the name of the directory containing root_dir.
        parent_of_root_abs_path = os.path.dirname(self._root_dir)
        # If root_dir is 'C:\', dirname is 'C:\'. If 'C:\folder', dirname is 'C:\'.
        # If root_dir is './my_folder', dirname is '.'.
        parent_of_root_display_name = os.path.basename(parent_of_root_abs_path) 
        if parent_of_root_abs_path == self._root_dir: # e.g. for C:\
             parent_of_root_display_name = "<root>" # Or some indicator it's the filesystem root
        elif parent_of_root_abs_path == os.getcwd() and not os.path.isabs(self._root_dir):
             parent_of_root_display_name = "." # If root_dir was relative like "my_folder"

        root_entry: DirectoryEntry = {
            "name": root_name,
            "path": ".", 
            "parent_directory": parent_of_root_display_name, 
            "type": "directory",
            "size_bytes": self._get_directory_size(self._root_dir)
        }
        self._collected_data.append(root_entry)

        for dirpath, dirnames, filenames in os.walk(self._root_dir, topdown=True):
            current_scan_dir_relative_path = os.path.relpath(dirpath, self._root_dir)
            # Parent for items directly under dirpath, relative to root_dir
            parent_for_children = current_scan_dir_relative_path.replace("\\\\", "/")

            for dirname in dirnames:
                full_subdir_path = os.path.join(dirpath, dirname)
                relative_subdir_path = os.path.relpath(full_subdir_path, self._root_dir)
                
                entry: DirectoryEntry = {
                    "name": dirname,
                    "path": relative_subdir_path.replace("\\\\", "/"),
                    "parent_directory": parent_for_children,
                    "type": "directory",
                    "size_bytes": self._get_directory_size(full_subdir_path)
                }
                self._collected_data.append(entry)

            for filename in filenames:
                full_file_path = os.path.join(dirpath, filename)
                relative_file_path = os.path.relpath(full_file_path, self._root_dir)
                
                try:
                    file_size = os.path.getsize(full_file_path)
                except FileNotFoundError:
                    print(f"Warning: File not found during scan: {full_file_path}")
                    file_size = 0 

                entry: DirectoryEntry = {
                    "name": filename,
                    "path": relative_file_path.replace("\\\\", "/"),
                    "parent_directory": parent_for_children,
                    "type": "file",
                    "size_bytes": file_size
                }
                self._collected_data.append(entry)
        
        self._collected_data.sort(key=lambda x: (x['path'] != '.', x['path'].count('/'), x['path']))
        return self._collected_data

    def get_collected_data(self) -> List[DirectoryEntry]:
        """Returns the collected directory scan data. Scans if not already done."""
        if not self._collected_data:
            self.scan_directory()
        return self._collected_data

    def save_to_json(self, output_filepath: str) -> None:
        """Saves the collected data to a JSON file."""
        data = self.get_collected_data()
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved directory scan to JSON: {output_filepath}")

    def save_to_csv(self, output_filepath: str) -> None:
        """Saves the collected data to a CSV file."""
        data = self.get_collected_data()
        if not data:
            print("No data to save to CSV.")
            return
        
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        fieldnames = list(DirectoryEntry.__annotations__.keys())
        with open(output_filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully saved directory scan to CSV: {output_filepath}")

    def save_to_pickle(self, output_filepath: str) -> None:
        """Saves the collected data to a Pickle file."""
        data = self.get_collected_data()
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, 'wb') as f:
            pickle.dump(data, f)
        print(f"Successfully saved directory scan to Pickle: {output_filepath}") 