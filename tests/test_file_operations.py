# tests/test_file_operations.py

import pytest
import json
from math_json_ops.file_operations import add_dict_to_list, delete_dict_from_list, read_json, write_json

@pytest.fixture
def setup_test_data(tmpdir):
    test_file = tmpdir.join('test.json')
    test_data = {
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
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    yield test_file

def test_read_json(setup_test_data):
    test_file = setup_test_data
    data = read_json(test_file)
    assert len(data["people"]) == 1
    assert data["people"][0]["name"] == "John Doe"

def test_add_dict_to_list(setup_test_data):
    test_file = setup_test_data
    new_dict = {
        "name": "Swati Dutta",
        "age": 31,
        "city": "Kathmandu",
        "country": "Nepal",
        "Education": "B.E"
    }
    add_dict_to_list(test_file, new_dict)
    data = read_json(test_file)
    assert len(data["people"]) == 2

def test_delete_dict_from_list(setup_test_data):
    test_file = setup_test_data
    delete_dict_from_list(test_file, 0)
    data = read_json(test_file)
    assert len(data["people"]) == 0
