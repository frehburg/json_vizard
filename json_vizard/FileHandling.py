from pathlib import Path
from typing import Union, Dict

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
    :raises ValueError: If the file is not a valid JSON or BSON file.
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
