import os
import glob
from typing import List

def read_file(file_path: str) -> str:
    """Reads and returns the content of a specified file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def list_directory(path: str) -> List[str]:
    """Lists the names of files and subdirectories in a directory."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error listing directory: {e}"]

def glob_files(pattern: str) -> List[str]:
    """Finds files matching a glob pattern recursively."""
    try:
        return glob.glob(pattern, recursive=True)
    except Exception as e:
        return [f"Error with glob pattern: {e}"]
