import pytest as pytest

from json_vizard import Hashing


@pytest.mark.skip(reason='Not implemented yet')
def test_hash_string_reproducible():
    string1 = 'Hello, World!'
    string2 = 'Hello, World!'
    hash1 = Hashing.unique_hash(string1)
    hash2 = Hashing.unique_hash(string2)

    assert hash1 == hash2


@pytest.mark.skip(reason='Not implemented yet')
def test_hash_string_different():
    string1 = 'Hello, World!'
    string2 = 'Hello, World'
    hash1 = Hashing.unique_hash(string1)
    hash2 = Hashing.unique_hash(string2)

    assert hash1 != hash2


@pytest.mark.skip(reason='Not implemented yet')
def test_hash_dict_reproducible():
    dict1 = {'Hello': 'World', 'Foo': 'Bar', 'Baz': {'Qux': 'Quux'}}
    dict2 = {'Hello': 'World', 'Foo': 'Bar', 'Baz': {'Qux': 'Quux'}}
    hash1 = Hashing.unique_hash(dict1)
    hash2 = Hashing.unique_hash(dict2)

    assert hash1 == hash2


@pytest.mark.skip(reason='Not implemented yet')
def test_hash_dict_different():
    dict1 = {'Hello': 'World', 'Foo': 'Bar', 'Baz': {'Qux': 'Quux'}}
    dict2 = {'Hello': 'World', 'Foo': 'Bar', 'Baz': {'Qux': 'Quuux'}}
    hash1 = Hashing.unique_hash(dict1)
    hash2 = Hashing.unique_hash(dict2)

    assert hash1 != hash2


@pytest.mark.skip(reason='Not implemented yet')
def test_compare_hashes_equal():
    hash1 = Hashing.unique_hash('Hello, World!')
    hash2 = Hashing.unique_hash('Hello, World!')

    assert Hashing.compare_hashes(hash1, hash2)


@pytest.mark.skip(reason='Not implemented yet')
def test_compare_not_hashes_equal():
    hash1 = Hashing.unique_hash('Hello, World!')
    hash2 = Hashing.unique_hash('Hello, World')

    assert not Hashing.compare_hashes(hash1, hash2)
