import pytest

a = "747465939"

b = "meow meow kitty cat"

c = "Croco Jack the crocodile"


@pytest.mark.parametrize('test_input1', ['m', 't', 'y', 'o', 'e', 'a'])
def test_string_count_check(test_input1):
    assert b.count(test_input1) == 2


def test_string_end_check():
    assert c.endswith('e') is True


def test_string_find_check():
    assert b.find('a') == 17


def test_string_index_check():
    assert b.index('w') == 3


def test_string_isdigit_check():
    assert a.isdigit()
