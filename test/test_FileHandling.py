import os
from pathlib import Path

import pytest

from json_vizard import read, write
from json_vizard.FileHandling import remove

deeply_nested = {
    "level_1": {
        "key_1": "value_1",
        "key_2": {
            "key_2_1": "value_2_1",
            "key_2_2": {
                "key_2_2_1": "value_2_2_1",
                "key_2_2_2": "value_2_2_2"
            }
        },
        "key_3": "value_3"
    },
    "level_2": {
        "key_4": {
            "key_4_1": {
                "key_4_1_1": "value_4_1_1"
            },
            "key_4_2": "value_4_2"
        },
        "key_5": "value_5"
    },
    "level_3": {
        "key_6": "value_6",
        "key_7": {
            "key_7_1": {
                "key_7_1_1": {
                    "key_7_1_1_1": "value_7_1_1_1"
                }
            },
            "key_7_2": "value_7_2"
        }
    }
}

empty_line_end_of_file = {
    "level1": "test",
    "level2": {
        "level3": "test"
    }
}

empty_line_in_between = {
    "level1": "test",
    "level2": {
        "level3": "test"
    }
}

lists = {
    "level1a": ["a", "b", "c"],
    "level1b": ["d", "e", "f"],
    "level1c": ["g", "h", "i"],
    "level1d": ["j", "k", "l"]
}

mixed_types = {
    "name": "Testface McTestson",
    "age": 99,
    "location": "Testville",
    "hobbies": ["testing1", "testing2", "testing3"],
    "likes": {
        "food": {
            "veggies": ["testing1veg", "testing2veg", "testing3veg"],
            "meat": ["testing1meat", "testing2meat", "testing3meat"]
        },
        "drink": ["testing1bev", "testing2bev", "testing3bev"],
        "color": "testing"
    }
}

numbers = {
    "level1a": 2.000000001,
    "level1b": 300000,
    "level1c": 4237948,
    "level1d": 5.9,
    "level1e": 0.000000000000000
}


def test_read_json_deeply_nested():
    path = Path.cwd() / 'test_data' / 'json' / 'deeply_nested.json'
    assert read(path) == deeply_nested


def test_read_bson_deeply_nested():
    path = Path.cwd() / 'test_data' / 'bson' / 'deeply_nested.bson'
    assert read(path) == deeply_nested


def test_read_txt_deeply_nested():
    path = Path.cwd() / 'test_data' / 'txt' / 'deeply_nested.txt'
    assert read(path) == deeply_nested


def test_read_json_empty_line_end_of_file():
    path = Path.cwd() / 'test_data' / 'json' / 'empty_line_end_of_file.json'
    assert read(path) == empty_line_end_of_file


def test_read_bson_empty_line_end_of_file():
    path = Path.cwd() / 'test_data' / 'bson' / 'empty_line_end_of_file.bson'
    assert read(path) == empty_line_end_of_file


def test_read_txt_empty_line_end_of_file():
    path = Path.cwd() / 'test_data' / 'txt' / 'empty_line_end_of_file.txt'
    assert read(path) == empty_line_end_of_file


def test_read_json_empty_line_in_between():
    path = Path.cwd() / 'test_data' / 'json' / 'empty_line_in_between.json'
    assert read(path) == empty_line_in_between


def test_read_bson_empty_line_in_between():
    path = Path.cwd() / 'test_data' / 'bson' / 'empty_line_in_between.bson'
    assert read(path) == empty_line_in_between


def test_read_txt_empty_line_in_between():
    path = Path.cwd() / 'test_data' / 'txt' / 'empty_line_in_between.txt'
    assert read(path) == empty_line_in_between


def test_read_json_lists():
    path = Path.cwd() / 'test_data' / 'json' / 'lists.json'
    assert read(path) == lists


def test_read_bson_lists():
    path = Path.cwd() / 'test_data' / 'bson' / 'lists.bson'
    assert read(path) == lists


def test_read_txt_lists():
    path = Path.cwd() / 'test_data' / 'txt' / 'lists.txt'
    assert read(path) == lists


def test_read_json_mixed_types():
    path = Path.cwd() / 'test_data' / 'json' / 'mixed_types.json'
    assert read(path) == mixed_types


def test_read_bson_mixed_types():
    path = Path.cwd() / 'test_data' / 'bson' / 'mixed_types.bson'
    assert read(path) == mixed_types


def test_read_txt_mixed_types():
    path = Path.cwd() / 'test_data' / 'txt' / 'mixed_types.txt'
    assert read(path) == mixed_types


def test_read_json_numbers():
    path = Path.cwd() / 'test_data' / 'json' / 'numbers.json'
    assert read(path) == numbers


def test_read_bson_numbers():
    path = Path.cwd() / 'test_data' / 'bson' / 'numbers.bson'
    assert read(path) == numbers


def test_read_txt_numbers():
    path = Path.cwd() / 'test_data' / 'txt' / 'numbers.txt'
    assert read(path) == numbers


@pytest.mark.skip(reason='Not implemented yet')
def test_write_json_deeply_nested():
    path = Path.cwd() / 'test_data' / 'temp' / 'deeply_nested.json'
    write(deeply_nested, path)
    assert read(path) == deeply_nested
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_bson_deeply_nested():
    path = Path.cwd() / 'test_data' / 'temp' / 'deeply_nested.bson'
    write(deeply_nested, path)
    assert read(path) == deeply_nested
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_txt_deeply_nested():
    path = Path.cwd() / 'test_data' / 'temp' / 'deeply_nested.txt'
    write(deeply_nested, path)
    assert read(path) == deeply_nested
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_json_empty_line_end_of_file():
    path = Path.cwd() / 'test_data' / 'temp' / 'empty_line_end_of_file.json'
    write(empty_line_end_of_file, path)
    assert read(path) == empty_line_end_of_file
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_bson_empty_line_end_of_file():
    path = Path.cwd() / 'test_data' / 'temp' / 'empty_line_end_of_file.bson'
    write(empty_line_end_of_file, path)
    assert read(path) == empty_line_end_of_file
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_txt_empty_line_end_of_file():
    path = Path.cwd() / 'test_data' / 'temp' / 'empty_line_end_of_file.txt'
    write(empty_line_end_of_file, path)
    assert read(path) == empty_line_end_of_file
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_json_empty_line_in_between():
    path = Path.cwd() / 'test_data' / 'temp' / 'empty_line_in_between.json'
    write(empty_line_in_between, path)
    assert read(path) == empty_line_in_between
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_bson_empty_line_in_between():
    path = Path.cwd() / 'test_data' / 'temp' / 'empty_line_in_between.bson'
    write(empty_line_in_between, path)
    assert read(path) == empty_line_in_between
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_txt_empty_line_in_between():
    path = Path.cwd() / 'test_data' / 'temp' / 'empty_line_in_between.txt'
    write(empty_line_in_between, path)
    assert read(path) == empty_line_in_between
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_json_lists():
    path = Path.cwd() / 'test_data' / 'temp' / 'lists.json'
    write(lists, path)
    assert read(path) == lists
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_bson_lists():
    path = Path.cwd() / 'test_data' / 'temp' / 'lists.bson'
    write(lists, path)
    assert read(path) == lists
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_txt_lists():
    path = Path.cwd() / 'test_data' / 'temp' / 'lists.txt'
    write(lists, path)
    assert read(path) == lists
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_json_mixed_types():
    path = Path.cwd() / 'test_data' / 'temp' / 'mixed_types.json'
    write(mixed_types, path)
    assert read(path) == mixed_types
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_bson_mixed_types():
    path = Path.cwd() / 'test_data' / 'temp' / 'mixed_types.bson'
    write(mixed_types, path)
    assert read(path) == mixed_types
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_txt_mixed_types():
    path = Path.cwd() / 'test_data' / 'temp' / 'mixed_types.txt'
    write(mixed_types, path)
    assert read(path) == mixed_types
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_json_numbers():
    path = Path.cwd() / 'test_data' / 'temp' / 'numbers.json'
    write(numbers, path)
    assert read(path) == numbers
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_bson_numbers():
    path = Path.cwd() / 'test_data' / 'temp' / 'numbers.bson'
    write(numbers, path)
    assert read(path) == numbers
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_write_txt_numbers():
    path = Path.cwd() / 'test_data' / 'temp' / 'numbers.txt'
    write(numbers, path)
    assert read(path) == numbers
    remove(path)


@pytest.mark.skip(reason='Not implemented yet')
def test_remove():
    path = Path.cwd() / 'test_data' / 'temp' / 'remove.json'
    data_dict = {'test': 'test'}

    write(data_dict, path)

    # assert os.path.exists(path)

    remove(path)

    assert not os.path.exists(path)
