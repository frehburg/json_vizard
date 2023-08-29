from typing import Dict


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
    :type dictionary: Dict
    :param args: The keys to remove the value from.
    :type args: Union[str, int]
    :param kwargs: Can be key or keys. Key is an index, keys is a list of indices.
    :return: True if the value was removed successfully, False otherwise.
    :rtype: bool
    :raises KeyError: If the key or keys do not exist in the dictionary.
    """
    pass