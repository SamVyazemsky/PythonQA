from pytest import mark


class StringMethodsTests:

    @mark.base
    def test_dict_clear(self, dict_123_str_to_int):
        """	Removes all the elements from the dictionary"""
        dict_123_str_to_int.clear()
        assert dict_123_str_to_int == {}

    @mark.base
    def test_dict_cope(self, dict_123_str_to_int):
        """Returns a copy of the dictionary"""
        test_dict = dict_123_str_to_int.copy()
        assert dict_123_str_to_int == test_dict
        assert id(dict_123_str_to_int) != id(test_dict)

    @mark.base
    def test_dict_keys(self, dict_123_str_to_int):
        """Returns a generator containing the dictionary's keys"""
        assert list(dict_123_str_to_int.keys()) == ["one", "two", "three"]

    @mark.base
    def test_dict_values(self, dict_123_str_to_int):
        """Returns a generator of all the values in the dictionary"""
        assert list(dict_123_str_to_int.values()) == [1, 2, 3]

    @mark.advance
    @mark.parametrize("key, value", [('one', 1), ('two', 2), ('three', 3)])
    def test_dict_get(self, dict_123_str_to_int, key, value):
        """Returns the value of the specified key"""
        assert dict_123_str_to_int.get(key) == value
