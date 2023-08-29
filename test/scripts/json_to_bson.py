import json
from pathlib import Path

import bson


def json_to_bson(json_path, bson_path):
    # Read JSON file
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Convert JSON to BSON and write to file
    with open(bson_path, 'wb') as bson_file:
        bson_data = bson.dumps(json_data)
        bson_file.write(bson_data)

    # Read BSON file
    with open(bson_path, 'rb') as bson_file:
        bson_data_read = bson_file.read()
        bson_dict = bson.loads(bson_data_read)

    return json_data, bson_dict


def main():
    json_path = Path.cwd() / 'test_data' / 'json'
    bson_path = Path.cwd() / 'test_data' / 'bson'

    file_names = [
        'deeply_nested',
        'empty_line_end_of_file',
        'empty_line_in_between',
        'lists',
        'mixed_types',
        'numbers'
    ]
    for file_name in file_names:
        source_path = json_path / (file_name + '.json')
        target_path = bson_path / (file_name + '.bson')
        json_dict, bson_dict = json_to_bson(source_path, target_path)

        print("Original JSON dictionary:")
        print(json_dict)
        print("\nDictionary from BSON:")
        print(bson_dict)


if __name__ == "__main__":
    main()
