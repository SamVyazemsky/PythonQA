import pytest


class TestDictionary:
    @pytest.mark.parametrize("key, value", [(1, 'one'), (4, 'no such element')])
    def test_check_get_method(self, key, value, dic):
        assert dic.get(key, 'no such element') == value

    def test_check_clear_method(self, dic):
        dic.clear()
        assert dic == {}

    @pytest.mark.parametrize("key, value", [(1, 'one'), (4, 'some')])
    def test_check_setdefault_method(self, key, value, dic):
        assert dic.setdefault(key, 'some') == value

    def test_check_popitem_method(self, dic):
        dic.popitem()
        assert len(dic) == 2

    def test_check_keys_method(self, dic):
        assert list(dic.keys()) == [1, 2, 3]


