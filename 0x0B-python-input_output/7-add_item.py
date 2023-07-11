#!/usr/bin/python3
'''

Load, add and save from argv

'''


import sys
import os

filename = "./add_item.json"
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
argv = sys.argv
if os.path.exists(filename):
    current_list = load_from_json_file("add_item.json")
    current_list.extend(argv[1:])
else:
    current_list = argv[1:]
save_to_json_file(current_list, "add_item.json")
