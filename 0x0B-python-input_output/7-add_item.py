#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
import os.path


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    filename = "add_item.json"

    # Check if the file exists, load its content if it does
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            try:
                items = json.load(file)
            except json.JSONDecodeError:
                items = []
    else:
        items = []

    items.extend(sys.argv[1:])

    # Save the updated list to the file
    with open(filename, 'w') as file:
        json.dump(items, file)
