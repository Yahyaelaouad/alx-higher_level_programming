#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists, load its content if it does
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to the file
save_to_json_file(my_list, filename)
