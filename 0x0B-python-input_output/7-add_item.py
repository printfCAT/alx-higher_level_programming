#!/usr/bin/python3
import sys
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
data = []
for arg in sys.argv[1:]:
    data.append(arg)
save(data, 'add_item.json')
load('add_item.json')
