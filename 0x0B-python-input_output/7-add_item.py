#!/usr/bin/python3
"""load, add, save"""
import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file
if os.path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
    items = []
arguments = sys.argv[1:]
items.extend(arguments)
save_to_json_file(items, "add_item.json")
