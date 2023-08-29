from typing import Union, Dict


def unique_hash(obj: Union[Dict, str]) -> str:
    """Hashes a dictionary or string using SHA256.

    Hashes a dictionary or string using SHA256. Returns the hash as a string.

    :param obj: The dictionary or string to hash.
    :type obj: Union[Dict, str]
    :return: The hash as a string.
    :rtype: str
    """
    pass


def _hash_string(string: str) -> str:
    """Hashes a string using SHA256.

    :param string: The string to hash.
    :type string: str
    :return: The hash as a string.
    :rtype: str
    """
    pass


def _hash_dict(dictionary: Dict) -> str:
    """Hashes a dictionary using SHA256.

    :param dictionary:
    :return:
    """


def compare_hashes(hash1: str, hash2: str) -> bool:
    """Compares two hashes.

    Returns true if the hashes are equal, false otherwise.
    :param hash1: The first hash.
    :type hash1: str
    :param hash2: The second hash.
    :type hash2: str
    """
