from typing import Union, Dict, List, Tuple


def get_from(
        dictionary: Dict, *args, **kwargs) \
        -> Union[int, float, str, bool, Dict, List]:
    """ Gets a value from a dictionary using a key or list of keys.
    *Example dictionary*:
    dict1 = {
      "name": "John Johnson",
      "age": 99,
      "location": "Testville",
      "likes": {
        "food": {
            "veggies": ["testing1veg", "testing2veg", "testing3veg"],
            "meat": ["testing1meat", "testing2meat", "testing3meat"]
        },
        "drink": ["testing1bev", "testing2bev", "testing3bev"],
        "color": "testing"
      }
    }

    *Example usage 1 (key)*:
    get_from(dict1, key="name")
    >>> "John Johnson"

    *Example usage 2 (list of keys)*:
    get_from(dict1, keys=["likes", "food", "veggies", 1])
    >>> "testing2veg"

    *Example usage 3 (keys)*:
    get_from(dict1, "likes", "food", "veggies", 1)
    >>> "testing2veg"

    :param dictionary: The dictionary to get the value from.
    :type dictionary: Dict
    :param args: The keys to get the value from.
    :type args: Union[str, int]
    :param kwargs: Can be key or keys. Key is an index, keys is a list of indices.
    :return: The value from the dictionary.
    :rtype: Union[int, float, str, bool, Dict, List, Tuple]
    :raises KeyError: If the key or keys do not exist in the dictionary.
    """


def search(dictionary: Dict,
           prompt: Union[str, int, float, bool, Dict, List],
           search_for_keys: bool = False,
           exact_match: bool = True,
           delta: float = 0
           ) -> Union[
                    Dict[
                        Union[Tuple[Union[str, int]], str],
                        Union[int, float, str, bool, Dict, List]
                    ],
                    bool
           ]:
    """Searches a dictionary for a value.

    Searches a dictionary for a value. Returns a dictionary where the key is a tuple of
    keys to get the value from the dictionary and the value is the value from the
    dictionary. If the tuple of keys has a length of 1, the key will be a string.

    Return false if no matches are found.

    If search_for_key is True, the function will search for the key instead of the
    value.

    Turning exact match on will affect search values in the following way:
    * `int`: Will only return values that are equal to the search value.
    * `float`: Values in a delta of the value will be considered equal.
    * `str`: Strings that contain the search value will be considered equal.
    * `bool`: Will only return values that are equal to the search value.
    * `dict`: Dictionaries that contain the search value will be considered equal.
    Meaning that the search value must be a subset of the dictionary.
    * `list`: Lists that contain the search value will be considered equal. Meaning
    that the search value must be a sublist of the list.

    If a float search is performed with a delta > 0, setting exact_match to False is
    not necessary.

    Example Usage:
        Example dictionary:
        dict1 = {
          "name": "John Johnson",\n
          "age": 99,\n
          "location": "Testville",\n
          "likes": {
            "food": {
                "vegetarian": ["testing1veg", "testing2veg", "testing3veg"],\n
                "carnivorous": ["meat_beef", "meat_chicken", "meat_pork"]\n
            },
            "drink": ["testing1bev", "testing2bev", "testing3bev"],\n
            "color": "testing"\n
          }
        }

        Example usage 1 (search_for_key=False, exact_match=True):
        search(dict1, "testing1veg")
        >>> {
            ("likes", "food", "vegetarian", 0): "testing1veg"
        }

        Example usage 2 (search_for_key=False, exact_match=False):
        search(dict1, "meat", exact_match=False)
        >>> {
            ("likes", "food", "carnivorous", 0): "meat_beef",
            ("likes", "food", "carnivorous", 1): "meat_chicken",
            ("likes", "food", "carnivorous", 2): "meat_pork"
        }

        Example usage 3 (search_for_key=True, exact_match=True):
        search(dict1, "vegetarian", search_for_key=True)
        >>> {
            ("likes", "food", "vegetarian"): ["testing1veg", "testing2veg",
            "testing3veg"]
        }

        Example usage 4 (search_for_key=True, exact_match=False):
        search(dict1, "ca", search_for_key=True, exact_match=False)
        >>> {
            ("likes", "food", "carnivorous"): ["meat_beef", "meat_chicken", "meat_pork"]
            ("location"): "Testville"
        }

        Example usage 5 (no matches):
        search(dict1, "hobbies")
        >>> False

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: Union[str, int, float, bool, Dict, List]
    :param search_for_keys: Whether to search for keys instead of values.
    :type search_for_keys: bool
    :param exact_match: Whether to perform an exact match.
    :type exact_match: bool
    :param delta: The delta for float searches.
    :type delta: float
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    :rtype: Union[
                    Dict[
                        Union[Tuple[Union[str, int]], str],
                        Union[int, float, str, bool, Dict, List]
                    ],
                    bool
           ]
    """
    pass


def _search_int(dictionary: Dict, prompt: int):
    """Searches a dictionary for an int value.

    ints cannot be searched as keys, therefore this method only searches for values.
    ints can only be searched exactly.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: int
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_str_exact(dictionary: Dict, prompt: str):
    """Searches a dictionary for an exactly matching str value.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: str
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_str_fuzzy(dictionary: Dict, prompt: str):
    """Searches a dictionary for a fuzzy matching str value.

    TODO: explain exact functionality

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: str
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_float_exact(dictionary: Dict, prompt: float):
    """Searches a dictionary for an exactly matching float value.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: float
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_float_with_delta(dictionary: Dict, prompt: float, delta: float):
    """Searches a dictionary for a float value with a delta.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: float
    :param delta: The delta for the float value.
    :type delta: float
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_bool(dictionary: Dict, prompt: bool):
    """Searches a dictionary for a bool value.

    bools cannot be searched as keys, therefore this method only searches for values.
    bools can only be searched exactly.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: bool
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_dict_exact(dictionary: Dict, prompt: Dict):
    """Searches a dictionary for an exactly matching dict value.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: Dict
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_dict_fuzzy(dictionary: Dict, prompt: Dict):
    """Searches a dictionary for a fuzzy matching dict value.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: Dict
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_list_exact(dictionary: Dict, prompt: List):
    """Searches a dictionary for an exactly matching list value.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: List
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass


def _search_list_fuzzy(dictionary: Dict, prompt: List):
    """Searches a dictionary for a fuzzy matching list value.

    :param dictionary: The dictionary to search.
    :type dictionary: Dict
    :param prompt: The value to search for.
    :type prompt: List
    :return: A dictionary where the key is a tuple of keys to get the value from the
    dictionary and the value is the value from the dictionary.
    """
    pass
