from pytest import mark


class StringMethodsTests:

    @mark.base
    def test_set_clear(self, set_123_int):
        """Removes all the elements from the set"""
        set_123_int.clear()
        assert set_123_int == set()

    @mark.base
    def test_set_difference(self, set_123_int, set_345_int):
        """Returns a set containing the difference between two or more sets"""
        assert set_123_int.difference(set_345_int) == {1, 2}
        assert set_345_int.difference(set_123_int) == {4, 5}

    @mark.base
    def test_set_union(self, set_123_int, set_345_int):
        """Return a set containing the union of sets"""
        assert set_123_int.union(set_345_int) == {1, 2, 3, 4, 5}

    @mark.base
    def test_set_add(self, set_123_int):
        """Adds an element to the set"""
        set_123_int.add(4)
        assert set_123_int == {1, 2, 3, 4}

    @mark.advance
    def test_set_remove(self, set_123_int, set_check):
        """Removes the specified element"""
        set_123_int.remove(set_check[0])
        assert set_123_int == set_check[1]
