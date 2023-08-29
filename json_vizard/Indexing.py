from typing import Union, Dict, List, Tuple


def get_from(
        dictionary: Dict, *args, **kwargs) \
        -> Union[int, float, str, bool, Dict, List, Tuple]:
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