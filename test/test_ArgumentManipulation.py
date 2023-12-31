import pytest

from json_vizard import remove_arg, modify_arg, add_arg


@pytest.mark.skip(reason='Not implemented yet')
def test_remove_kwargs_key():
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
def test_remove_kwargs_keys():
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
def test_remove_args():
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

@pytest.mark.skip(reason='Not implemented yet')
def test_modify_kwargs_key():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    modify_arg(dict1, new_val="John Johnson Jr.", key="name")
    assert dict1 == {
        "name": "John Johnson Jr.",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_kwargs_keys():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    modify_arg(dict1, new_val="Test City", keys=["location", "work"])
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Test City"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_args():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    modify_arg(dict1, "Test City", "location", "work")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Test City"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_int():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    modify_arg(dict1, 100, "age")
    assert dict1 == {
        "name": "John Johnson",
        "age": 100,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_float():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    modify_arg(dict1, 100.1, "age")
    assert dict1 == {
        "name": "John Johnson",
        "age": 100.1,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_bool():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "is_human": True,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    modify_arg(dict1, False, "is_human")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "is_human": False,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_dict():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "is_human": True,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    new_locations = {
        "dwellings": {
            "primary": "Test City",
            "secondary": "Test Town"
        },
        "work": "Testington"
    }
    modify_arg(dict1, new_val=new_locations, key="location")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "is_human": True,
        "location": {
            "dwellings": {
                "primary": "Test City",
                "secondary": "Test Town"
            },
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_modify_list():
    dict1 = {
        "name": "John Johnson",
        "age": 99,
        "is_human": True,
        "location": {
            "home": "Testville",
            "work": "Testington"
        }
    }
    new_locations = ["Test City", "Test Town"]
    modify_arg(dict1, new_val=new_locations, key="location")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99,
        "is_human": True,
        "location": ["Test City", "Test Town"]
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_add_int():
    dict1 = {
        "name": "John Johnson",
    }
    add_arg(dict1, 99, "age")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_add_float():
    dict1 = {
        "name": "John Johnson",
    }
    add_arg(dict1, 99.1, "age")
    assert dict1 == {
        "name": "John Johnson",
        "age": 99.1
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_add_bool():
    dict1 = {
        "name": "John Johnson",
    }
    add_arg(dict1, True, "is_human")
    assert dict1 == {
        "name": "John Johnson",
        "is_human": True
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_add_dict():
    dict1 = {
        "name": "John Johnson",
    }
    locations = {
        "dwellings": {
            "primary": "Test City",
            "secondary": "Test Town"
        },
        "work": "Testington"
    }
    add_arg(dict1, new_val=locations, key="location")
    assert dict1 == {
        "name": "John Johnson",
        "location": {
            "dwellings": {
                "primary": "Test City",
                "secondary": "Test Town"
            },
            "work": "Testington"
        }
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_add_list():
    dict1 = {
        "name": "John Johnson",
    }
    locations = ["Test City", "Test Town"]
    add_arg(dict1, new_val=locations, key="location")
    assert dict1 == {
        "name": "John Johnson",
        "location": ["Test City", "Test Town"]
    }


@pytest.mark.skip(reason='Not implemented yet')
def test_add_deep():
    dict1 = {
        "name": "John Johnson",
        "location": {
            "private": {
                "vacation_homes" : {
                    "beach": "Test Beach",
                }
            }
        }
    }

    add_arg(
        dict1,
        new_val="Mount Testmore",
        keys=["location", "private", "vacation_homes", "mountain"]
    )

    assert dict1 == {
        "name": "John Johnson",
        "location": {
            "private": {
                "vacation_homes" : {
                    "beach": "Test Beach",
                    "mountain": "Mount Testmore"
                }
            }
        }
    }
