from pytest import mark


class ListMethodsTests:

    @mark.usefixtures('set_time')
    @mark.base
    def test_list_append(self, empty_list):
        """Adds an element at the end of the list"""
        empty_list.append(1)
        assert empty_list == [1]

    @mark.base
    def test_list_copy(self, list_123_int):
        """Returns a copy of the list"""
        test_list = list_123_int.copy()
        assert list_123_int == test_list
        assert id(list_123_int) != test_list

    @mark.base
    def test_list_reverse(self, list_123_int):
        """Reverses the order of the list"""
        list_123_int.reverse()
        assert list_123_int == [3, 2, 1]

    @mark.base
    def test_list_count(self, list_123_int):
        """Returns the number of elements with the specified value"""
        assert list_123_int.count(3) == 1

    @mark.advance
    def test_list_index(self, list_123_int, range_to_2):
        """Returns the index of the first element with the specified value"""
        assert list_123_int.index(range_to_2 + 1) == range_to_2
