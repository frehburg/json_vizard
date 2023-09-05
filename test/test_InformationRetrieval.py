import pytest

from json_vizard import get_from, search, traverse


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


def test_indexing_kwargs_key():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    assert get_from(dict1, key='a') == 1


@pytest.mark.skip(reason='Not implemented yet')
def test_search_exact_int():
    dict1 = {
        "age": 90,
        "year_born": 1933
    }
    assert search(dict1, 90) == {'age': 90}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_exact_str():
    dict1 = {
        "name": "John Johnson",
        "son": "John Johnson Jr.",
    }
    assert search(dict1, "John Johnson") == {'name': 'John Johnson'}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_exact_float():
    dict1 = {
        "pi": 3.14159265359,
        "e": 2.71828182846
    }
    assert search(dict1, 3.14159265359) == {'pi': 3.14159265359}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_exact_bool():
    dict1 = {
        "is_true": True,
        "is_false": False
    }
    assert search(dict1, True) == {'is_true': True}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_exact_list():
    dict1 = {
        "list1": [1, 2, 3],
        "list2": [4, 5, 6]
    }
    assert search(dict1, [1, 2, 3]) == {'list1': [1, 2, 3]}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_exact_dict():
    dict1 = {
        "dict1": {
            "key1": "value1",
            "key2": "value2"
        },
        "dict2": {
            "key3": "value3",
            "key4": "value4"
        }
    }
    assert search(dict1, {"key1": "value1", "key2": "value2"}) \
           == {'dict1': {'key1': 'value1', 'key2': 'value2'}}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_not_exact_int():
    dict1 = {
        "age": 90,
        "year_born": 1933
    }
    assert search(dict1, 90, exact_match=False) == {'age': 90}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_not_exact_str():
    dict1 = {
        "name": "John Johnson",
        "son": "John Johnson Jr.",
    }
    assert search(dict1, "John Johnson", exact_match=False) \
           == {
               'name': 'John Johnson',
               'son': 'John Johnson Jr.'
           }


@pytest.mark.skip(reason='Not implemented yet')
def test_search_not_exact_float():
    dict1 = {
        "pi": 3.14159265359,
        "pi_approx": 3.142
    }
    delta = 0.001
    assert search(dict1, 3.14159265359, delta=delta, exact_match=False) \
           == {
               'pi': 3.14159265359,
               'pi_approx': 3.142
           }


@pytest.mark.skip(reason='Not implemented yet')
def test_search_delta_without_exact_match_false():
    dict1 = {
        "pi": 3.14159265359,
        "pi_approx": 3.142
    }
    delta = 0.001
    assert search(dict1, 3.14159265359, delta=delta) \
           == {
               'pi': 3.14159265359,
               'pi_approx': 3.142
           }


@pytest.mark.skip(reason='Not implemented yet')
def test_search_not_exact_bool():
    dict1 = {
        "is_true": True,
        "is_false": False
    }
    assert search(dict1, True, exact_match=False) == {'is_true': True}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_not_exact_list():
    dict1 = {
        "list1": [1, 2, 3],
        "list2": [4, 5, 6]
    }
    assert search(dict1, [1, 2], exact_match=False) == {'list1': [1, 2, 3]}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_not_exact_dict():
    dict1 = {
        "dict1": {
            "key1": "value1",
            "key2": "value2"
        },
        "dict2": {
            "key3": "value3",
            "key4": "value4"
        }
    }
    assert search(dict1, {"key1": "value1"}, exact_match=False) \
           == {'dict1': {'key1': 'value1', 'key2': 'value2'}}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_key_exact_inexplicit():
    dict1 = {
        "name": "John Johnson",
        "son": "John Johnson Jr.",
    }
    assert search(dict1, "name", search_for_keys=True) == {'name': 'John Johnson'}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_key_exact_explicit():
    dict1 = {
        "name": "John Johnson",
        "son": "John Johnson Jr.",
    }
    assert search(dict1, "name", search_for_keys=True, exact_match=True) \
           == {'name': 'John Johnson'}


@pytest.mark.skip(reason='Not implemented yet')
def test_search_key_not_exact():
    dict1 = {
        "name": "John Johnson",
        "son": "John Johnson Jr.",
    }
    assert search(dict1, "nam", search_for_keys=True, exact_match=False) \
           == {'name': 'John Johnson'}


@pytest.mark.skip(reason='Not implemented yet')
def test_dfs_traverse_no_keys():
    dict1 = {
        "A": 1,
        "B_sub": {
            "B": 2,
            "D_sub": {
                "D": 4,
            },
        },
        "C_sub": {
            "C": 3,
            "EF_sub": {
                "E": 5,
                "F": 6,
            },
        },
    }

    expected_dfs_result = [1, 2, 4, 3, 5, 6]

    assert traverse(dict1, traversal_type='dfs') == expected_dfs_result
    assert traverse(dict1, traversal_type='dfs', include_keys=False) \
           == expected_dfs_result


@pytest.mark.skip(reason='Not implemented yet')
def test_dfs_traverse_keys():
    dict1 = {
        "A": 1,
        "B_sub": {
            "B": 2,
            "D_sub": {
                "D": 4,
            },
        },
        "C_sub": {
            "C": 3,
            "EF_sub": {
                "E": 5,
                "F": 6,
            },
        },
    }

    assert traverse(dict1, traversal_type='dfs', include_keys=True) \
           == [("A", 1), (["B_sub", "B"], 2), (["B_sub", "D_sub", "D"], 4),
               (["C_sub", "C"], 3), (["C_sub", "EF_sub", "E"], 5),
               (["C_sub", "EF_sub", "F"], 6)]


@pytest.mark.skip(reason='Not implemented yet')
def test_bfs_traverse_no_keys():
    dict1 = {
        "A": 1,
        "B_sub": {
            "B": 2,
            "D_sub": {
                "D": 4,
            },
        },
        "C_sub": {
            "C": 3,
            "EF_sub": {
                "E": 5,
                "F": 6,
            },
        },
    }

    expected_bfs_result = [1, 2, 3, 4, 5, 6]

    assert traverse(dict1) == expected_bfs_result
    assert traverse(dict1, traversal_type='bfs') == expected_bfs_result
    assert traverse(dict1, traversal_type='bfs', include_keys=False) \
           == expected_bfs_result


@pytest.mark.skip(reason='Not implemented yet')
def test_bfs_traverse_keys():
    dict1 = {
        "A": 1,
        "B_sub": {
            "B": 2,
            "D_sub": {
                "D": 4,
            },
        },
        "C_sub": {
            "C": 3,
            "EF_sub": {
                "E": 5,
                "F": 6,
            },
        },
    }

    expected_bfs_result = [("A", 1), (["B_sub", "B"], 2), (["C_sub", "C"], 3),
                           (["B_sub", "D_sub", "D"], 4), (["C_sub", "EF_sub", "E"], 5),
                           (["C_sub", "EF_sub", "F"], 6)]

    assert traverse(dict1, include_keys=True) \
           == expected_bfs_result
    assert traverse(dict1, traversal_type='bfs', include_keys=True) \
           == expected_bfs_result
