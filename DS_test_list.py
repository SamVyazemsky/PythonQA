import pytest

test_data_list1 = [1, 2, 3, 456, 7899]

test_data_list2 = [10, 22, 25, 983]


def test_list_del_element():
    test_data_list1.pop(0)
    assert len(test_data_list1) == 4


def test_list_count_element():
    assert test_data_list1.count(456) == 1


def test_list_add_element():
    test_data_list1.append(999)
    assert len(test_data_list1) == 5


def test_list_insert_element():
    test_data_list1.insert(1, 222)
    assert test_data_list1.count(222) == 1


@pytest.mark.parametrize('test_input,expected', [(test_data_list1, test_data_list1), (test_data_list1, test_data_list2),
                                                 (test_data_list2, 8), (test_data_list2, test_data_list2)])
def test_eval(test_input, expected):
    assert test_input is expected


@pytest.mark.parametrize('test_index,test_input', [(0, 456), (1, 321),
                                                   (2, 8)])
def test_list_insert_parametrized_element(test_index, test_input):
    test_data_list1.insert(test_index, test_input)
    test_data_list2.insert(test_index, test_input)
    assert len(test_data_list1) < len(test_data_list2)
