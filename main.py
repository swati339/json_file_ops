from math_json_ops.file_operations import add_dict_to_list, delete_dict_from_list, read_json, write_json

def main():
    file_path = 'C:/Users/Dell Inspiron 7306/OneDrive/Desktop/math_json_ops/math_json_ops/data/sample.json'

    # Initial data
    initial_data = {
        "people": [
            {
                "name": "John Doe",
                "age": 30,
                "city": "New York",
                "country": "USA",
                "Education": "BCA"
            }
        ]
    }
    write_json(file_path, initial_data)
    print("Initial data:", read_json(file_path))

    # Adding new dictionary
    new_dict = {
        "name": "Swati Dutta",
        "age": 31,
        "city": "Kathmandu",
        "country": "Nepal",
        "Education": "B.E"
    }
    add_dict_to_list(file_path, new_dict)
    print("After adding new dict:", read_json(file_path))

    # Deleting a dictionary
    delete_dict_from_list(file_path, 0)
    print("After deleting dict:", read_json(file_path))

if __name__ == "__main__":
    main()
