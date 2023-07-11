#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"

    # Check if the file exists, load its content if it does
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)
