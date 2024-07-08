import pytest
from math_json_ops.file_operations import read_json, write_json, update_json, get_data_directory
from pathlib import Path

@pytest.fixture
def test_file():
    data_dir = get_data_directory()
    data_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    test_file = data_dir / 'test.json'
    yield test_file
    if test_file.exists():
        test_file.unlink()

def test_write_json(test_file):
    data = {
        "name": "Test User",
        "age": 99,
        "city": "Test City",
        "country": "Test Country",
        "Education": "Test Education"
    }
    write_json(test_file, data)
    assert test_file.exists()

def test_read_json(test_file):
    data = {
        "name": "Test User",
        "age": 99,
        "city": "Test City",
        "country": "Test Country",
        "Education": "Test Education"
    }
    write_json(test_file, data)
    data_read = read_json(test_file)
    assert data_read == data

def test_update_json(test_file):
    data = {
        "name": "Test User",
        "age": 99,
        "city": "Test City",
        "country": "Test Country",
        "Education": "Test Education"
    }
    write_json(test_file, data)
    update_json(test_file, "age", 100)
    data_read = read_json(test_file)
    assert data_read["age"] == 100
