from typing import Union, Dict
import hashlib


def unique_hash(obj: Union[Dict, str]) -> str:
    """Hashes a dictionary or string using SHA256.

    Hashes a dictionary or string using SHA256. Returns the hash as a string.

    :param obj: The dictionary or string to hash.
    :type obj: Union[Dict, str]
    :return: The hash as a string.
    :rtype: str
    :raises TypeError: If obj is not a dictionary or string.
    """
    if isinstance(obj, str):
        return _hash_string(obj)
    elif isinstance(obj, dict):
        return _hash_dict(obj)
    else:
        raise TypeError('obj must be a dictionary or string.')


def _hash_string(string: str) -> str:
    """Hashes a string using SHA256.

    :param string: The string to hash.
    :type string: str
    :return: The hash as a string.
    :rtype: str
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


def _hash_dict(dictionary: Dict) -> str:
    """Hashes a dictionary using SHA256.

    :param dictionary:
    :return:
    """
    dictionary_string = str(dictionary)
    return _hash_string(dictionary_string)


def compare_hashes(hash1: str, hash2: str) -> bool:
    """Compares two hashes.

    Returns true if the hashes are equal, false otherwise.
    :param hash1: The first hash.
    :type hash1: str
    :param hash2: The second hash.
    :type hash2: str
    :return: True if the hashes are equal, false otherwise.
    :rtype: bool
    """
    return hash1 == hash2
