

import json
from pathlib import Path

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_json(file_path, key, value):
    data = read_json(file_path)
    data[key] = value
    write_json(file_path, data)

def get_project_root():
    return Path(__file__).parent.parent

def get_data_directory():
    return get_project_root() / 'math_json_ops' / 'data'

def main():
    data_dir = get_data_directory()
    sample_file = data_dir / 'sample.json'

    # Writing JSON data to file
    data_to_write = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    write_json(sample_file, data_to_write)
    print(f"Data written to {sample_file}")

    # Reading JSON data from file
    data_read = read_json(sample_file)
    print(f"Data read from {sample_file}:")
    print(data_read)

    # Updating JSON data in file
    update_json(sample_file, "age", 31)
    data_updated = read_json(sample_file)
    print(f"Data after update in {sample_file}:")
    print(data_updated)

if __name__ == '__main__':
    main()
