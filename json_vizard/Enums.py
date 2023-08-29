from enum import Enum


class ReturnType(Enum):
    DICT = 'dict_return_type_enum'
    STRING = 'string_return_type_enum'


class FileType(Enum):
    JSON = 'json_file_type_enum'
    BSON = 'bson_file_type_enum'
    TXT = 'txt_file_type_enum'

