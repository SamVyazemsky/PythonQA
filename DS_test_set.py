import pytest

test_data_set1 = {'charmander', 'meow', 'charmander', 'zealot'}
test_data_set2 = {'pikapika', 'auff', 'pikapika', 'zealot'}

A = {1, 2, 3}
B = {3, 2, 5, 1}


def test_set_remove_element():
    test_data_set1.remove('charmander')
    assert 'charmander' not in test_data_set1


def test_set_union_check():
    result = A.union(B)
    assert 5 in result


@pytest.mark.parametrize('test_input1, test_input2', [(777, 456), (456, 321),
                                                      (7765, 54567)])
def test_set_parametrized_add_element(test_input1, test_input2):
    A.add(test_input1)
    A.add(test_input2)
    assert test_input1 and test_input2 in A


def test_set_intersection_check():
    assert 'zelot777' in test_data_set1.intersection(test_data_set2)


def test_set_diff_check():
    assert 'auff' in test_data_set2.difference(test_data_set1)
