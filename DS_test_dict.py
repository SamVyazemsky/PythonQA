import pytest

test_data_dict1 = {'player1': 200, 'player2': 400, 'player3': 900}

test_data_dict2 = {'owner1': 30000, 'owner2': 1000, 'owner3': 9200}


def test_dict_update_check():
    test_data_dict1.update({'player5': 8000,
                            'player6': 777})
    dict1_expected = {'player6': 777, 'player1': 200, 'player5': 8000, 'player2': 400, 'player3': 900}

    assert test_data_dict1 == dict1_expected


@pytest.mark.parametrize('test_input1', ['owner', 'owner1', 'owner2', 'owner22445', 'owner3', '32167'])
def test_parametrized_get_key_check(test_input1):
    assert test_data_dict2.get(test_input1, 'this key is missed') == 'this key is missed'


def test_dict_pop_check():
    assert test_data_dict1.pop('player6') == 777


def test_dict_value_check():
    assert test_data_dict2.values() == [1000, 9200, 30000]


def test_dict_popitem_check():
    dict1_expected = ('player1', 200)
    assert test_data_dict1.popitem() == dict1_expected
