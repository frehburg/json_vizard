from pathlib import Path
from typing import Union, Dict
import json

from json_vizard.Enums import ReturnType, FileType


def read(path: Path, return_type: ReturnType = ReturnType.DICT) -> Union[dict, str]:
    """Reads a dictionary from a JSON, BSON or TXT file.

    Can read JSON, BSON and TXT files. Returns a dictionary or string, depending on the
    value of to_datatype. Can be either ReturnType.DICT or ReturnType.STRING.

    :param path: Path to the JSON or BSON file.
    :type path: Path
    :param return_type: Either ReturnType.DICT or ReturnType.STRING.
    :type return_type: ReturnType
    :return: The JSON or BSON file as a dictionary or string.
    :rtype: Union[dict, str]
    :raises TypeError: If to_datatype is not a ReturnType.
    :raises FileNotFoundError: If the file does not exist.
    :raises JSONDecodeError: If the file is not a valid JSON file.
    """
    if not isinstance(return_type, ReturnType):
        raise TypeError(f'return_type must be a ReturnType, not {type(return_type)}.')

    file_extension = path.suffix
    if file_extension == '.json':
        return _read_json(path, return_type)
    elif file_extension == '.bson':
        return _read_bson(path, return_type)
    elif file_extension == '.txt':
        return _read_txt(path, return_type)
    else:
        raise ValueError(f'File extension {file_extension} is not supported.')


def _read_json(path: Path, return_type: ReturnType = ReturnType.DICT)\
        -> Union[dict, str]:
    """Reads a dictionary from a JSON file.

    :param path: Path to the JSON file.
    :type path: Path
    :return: The JSON file as a dictionary.
    :rtype: Union[dict, str]
    :raises FileNotFoundError: If the file does not exist.
    :raises JSONDecodeError: If the file is not a valid JSON file.
    """
    with open('data.json', 'r') as json_file:
        dictionary = json.load(json_file)

    if return_type == ReturnType.DICT:
        return dictionary
    elif return_type == ReturnType.STRING:
        return json.dumps(dictionary)


def _read_bson(path: Path, return_type: ReturnType = ReturnType.DICT)\
        -> Union[dict, str]:
    """Reads a dictionary from a BSON file.

    :param path: Path to the BSON file.
    :type path: Path
    :return: The BSON file as a dictionary.
    :rtype: Union[dict, str]
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file is not a valid BSON file.
    """
    pass


def _read_txt(path: Path, return_type: ReturnType = ReturnType.DICT)\
        -> Union[dict, str]:
    """Reads a dictionary from a TXT file.

    :param path: Path to the TXT file.
    :type path: Path
    :return: The TXT file as a dictionary.
    :rtype: Union[dict, str]
    :raises FileNotFoundError: If the file does not exist.
    """
    pass


def write(dictionary: Dict, path: Path, file_type=FileType.JSON) -> bool:
    """Writes a dictionary to a JSON file.

    Can write JSON, BSON and TXT files. Returns True if the file was written
    successfully,
    False otherwise.

    :param dictionary: The dictionary to write to the file.
    :type dictionary: Dict
    :param path: The path to the file.
    :type path: Path
    :param file_type: Either FileType.JSON, FileType.BSON or FileType.TXT.
    :type file_type: FileType
    :return: True if the file was written successfully, False otherwise.
    :rtype: bool
    :raises TypeError: If file_type is not a FileType.
    """
    pass


def _write_json(dictionary: Dict, path: Path) -> bool:
    """Writes a dictionary to a JSON file.

    :param dictionary: The dictionary to write to the file.
    :type dictionary: Dict
    :param path: The path to the file.
    :type path: Path
    :return: True if the file was written successfully, False otherwise.
    :rtype: bool
    """
    pass


def _write_bson(dictionary: Dict, path: Path) -> bool:
    """Writes a dictionary to a BSON file.

    :param dictionary: The dictionary to write to the file.
    :type dictionary: Dict
    :param path: The path to the file.
    :type path: Path
    :return: True if the file was written successfully, False otherwise.
    :rtype: bool
    """
    pass


def _write_txt(dictionary: Dict, path: Path) -> bool:
    """Writes a dictionary to a TXT file.

    :param dictionary: The dictionary to write to the file.
    :type dictionary: Dict
    :param path: The path to the file.
    :type path: Path
    :return: True if the file was written successfully, False otherwise.
    :rtype: bool
    """
    pass


def remove(path: Path) -> bool:
    """Removes a file.

    :param path: Path to the file.
    :type path: Path
    :return: True if the file was removed successfully, False otherwise.
    :rtype: bool
    """
    pass
