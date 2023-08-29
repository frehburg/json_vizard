import pytest

from json_vizard import get_from


@pytest.mark.skip(reason='Not implemented yet')
def test_deep_indexing_args():
    dict1 = {
        "level_1": {
            "key_1": "value_1",
            "key_2": {
                "key_2_1": "value_2_1",
                "key_2_2": {
                    "key_2_2_1": "value_2_2_1",
                    "key_2_2_2": "value_2_2_2"
                }
            },
            "key_3": "value_3"
        }
    }
    assert get_from(dict1, "level_1", "key_2", "key_2_2", "key_2_2_2") == "value_2_2_2"


@pytest.mark.skip(reason='Not implemented yet')
def test_deep_indexing_kwargs_keys():
    dict1 = {
        "level_1": {
            "key_1": "value_1",
            "key_2": {
                "key_2_1": "value_2_1",
                "key_2_2": {
                    "key_2_2_1": "value_2_2_1",
                    "key_2_2_2": "value_2_2_2"
                }
            },
            "key_3": "value_3"
        }
    }
    keys = ["level_1", "key_2", "key_2_2", "key_2_2_2"]
    assert get_from(dict1, keys=keys) == "value_2_2_2"


@pytest.mark.skip(reason='Not implemented yet')
def test_indexing_kwargs_key():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    assert get_from(dict1, key='a') == 1