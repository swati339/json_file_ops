import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_dict_to_list(file_path, new_dict):
    data = read_json(file_path)
    if "people" not in data:
        data["people"] = []
    data["people"].append(new_dict)
    write_json(file_path, data)

def delete_dict_from_list(file_path, index):
    data = read_json(file_path)
    if "people" in data and 0 <= index < len(data["people"]):
        data["people"].pop(index)
        write_json(file_path, data)
