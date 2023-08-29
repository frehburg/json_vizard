import pytest

from json_vizard.ArgumentManipulation import remove_arg


@pytest.mark.skip(reason='Not implemented yet')
def test_kwargs_key():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    remove_arg(dict1, key="name")
    assert dict1 == {
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_kwargs_keys():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    remove_arg(dict1, keys=["location", "home"])
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_args():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    remove_arg(dict1, "location", "home")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "work": "Testington"
        }
    }