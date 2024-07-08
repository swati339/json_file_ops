from math_json_ops.file_operations import read_json, write_json, update_json, get_data_directory
from pathlib import Path

def main():
    data_dir = get_data_directory()
    sample_file = data_dir / 'sample.json'

    # Read existing data
    existing_data = read_json(sample_file)
    print(f"Data read from {sample_file}:")
    print(existing_data)

    # Update data
    update_json(sample_file, 'age', 31)
    updated_data = read_json(sample_file)
    print(f"Data after update in {sample_file}:")
    print(updated_data)

if __name__ == '__main__':
    main()
