from typing import Dict, Union, List


def add_arg(dictionary: Dict,
            new_val: Union[int, float, str, bool, Dict, List],
            *args, **kwargs) -> bool:
    """Adds a value to a dictionary using a key or list of keys.

    Examples:
        Example dictionary:
            dict1 = {
                "name": "John Johnson",\n
                "age": 99,\n
                "location": {
                    "home": "Testville",\n
                    "work": "Testington"
                }\n
            }

        Example usage 1 (key):
            add_arg(dict1, new_val="Meridith Johnson", key="spouse")\n
            >>> True\n
            print(dict1)\n
            >>> {
                    "name": "John Johnson",\n
                    "age": 99,\n
                    "location": {
                        "home": "Testville",\n
                        "work": "Testington"
                    },\n
                    "spouse": "Meridith Johnson"
            }

        Example usage 2 (list of keys):
            add_arg(dict1, new_val="Test City", keys=["location", "second work"])\n
            >>> True\n
            print(dict1)\n
            >>> {
                    "name": "John Johnson",\n
                    "age": 99,\n
                    "location": {\n
                        "home": "Testville",\n
                        "work": "Testington",\n
                        "second work": "Test City"
                    },
            }

        Example usage 3 (keys):
            add_arg(dict1, new_val="Test City", "location", "second work")\n
            >>> True\n
            print(dict1)\n
            >>> {
                    "name": "John Johnson",\n
                    "age": 99,\n
                    "location": {
                        "home": "Testville",\n
                        "work": "Testington",\n
                        "second work": "Test City"\n
                    },
            }

    :param dictionary: The dictionary to add the value to.
    :traversal_type dictionary: Dict
    :param new_val: The new value.
    :traversal_type new_val: Union[int, float, str, bool]
    :param args: The keys to add the value to.
    :traversal_type args: Union[str, int]
    :param kwargs: Can be key or keys. Key is an index, keys is a list of indices.
    :return: True if the value was added successfully, False otherwise.
    :rtype: bool
    :raises KeyError: If the key or keys do not exist in the dictionary.
    """
    pass


def remove_arg(dictionary: Dict, *args, **kwargs) -> bool:
    """Removes a value from a dictionary using a key or list of keys.

    *Example dictionary*:
    dict1 = {
      "name": "John Johnson",
      "age": 99,
      "location": {
        "home": "Testville",
        "work": "Testington"
      }
    }

    *Example usage 1 (key)*:
    remove_arg(dict1, key="name")
    >>> True
    print(dict1)
    >>> {
            "age": 99,
            "location": {
               "home": "Testville",
               "work": "Testington"
            }
        }

    *Example usage 2 (list of keys)*:
    remove_arg(dict1, keys=["location", "home"])
    >>> True
    print(dict1)
    >>> dict1 = {
      "name": "John Johnson",
      "age": 99,
      "location": {
        "work": "Testington"
      }
    }

    *Example usage 3 (keys)*:
    remove_arg(dict1, "location", "home")
    >>> True
    print(dict1)
    >>> dict1 = {
      "name": "John Johnson",
      "age": 99,
      "location": {
        "work": "Testington"
      }
    }

    :param dictionary: The dictionary to remove the value from.
    :traversal_type dictionary: Dict
    :param args: The keys to remove the value from.
    :traversal_type args: Union[str, int]
    :param kwargs: Can be key or keys. Key is an index, keys is a list of indices.
    :return: True if the value was removed successfully, False otherwise.
    :rtype: bool
    :raises KeyError: If the key or keys do not exist in the dictionary.
    """
    pass


def modify_arg(
        dictionary: Dict,
        new_val: Union[int, float, str, bool, Dict, List],
        *args, **kwargs) -> bool:
    """Modifies a value in a dictionary using a key or list of keys.

    *Example dictionary*:
    dict1 = {
      "name": "John Johnson",
      "age": 99,
      "location": {
        "home": "Testville",
        "work": "Testington"
      }
    }

    *Example usage 1 (key)*:
    modify_simple_arg(dict1, new_val="John Johnson Jr.", key="name")
    >>> True
    print(dict1)
    >>> {
            "name": "John Johnson Jr.",
            "age": 99,
            "location": {
                "home": "Testville",
                "work": "Testington"
            }
        }

    *Example usage 2 (list of keys)*:
    modify_simple_arg(dict1, new_val="Test City", keys=["location", "work"])
    >>> True
    print(dict1)
    >>> {
            "name": "John Johnson",
            "age": 99,
            "location": {
                "home": "Testville",
                "work": "Test City"
            }
        }

    *Example usage 3 (keys)*:
    modify_simple_arg(dict1, new_val="Test City", "location", "work")
    >>> True
    print(dict1)
    >>> {
            "name": "John Johnson",
            "age": 99,
            "location": {
                "home": "Testville",
                "work": "Test City"
            }
        }

    :param dictionary: The dictionary to modify the value in.
    :traversal_type dictionary: Dict
    :param new_val: The new value.
    :traversal_type new_val: Union[int, float, str, bool]
    :param args: The keys to modify the value in.
    :traversal_type args: Union[str, int]
    :param kwargs: Can be key or keys. Key is an index, keys is a list of indices.
    :return: True if the value was modified successfully, False otherwise.
    :rtype: bool
    :raises KeyError: If the key or keys do not exist in the dictionary.
    """
    # TODO: implement as 1. remove_arg, 2. add_arg
    pass
