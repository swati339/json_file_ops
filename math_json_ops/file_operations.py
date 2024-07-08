import json
from pathlib import Path

def get_data_directory():
    return Path(__file__).parent / 'data'

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_json(file_path, key, value):
    data = read_json(file_path)
    data[key] = value
    write_json(file_path, data)
