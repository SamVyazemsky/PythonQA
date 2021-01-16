import pytest


class TestSet:
    @pytest.mark.parametrize("a, b, dif", [({1, 2, 3}, {2, 3}, {1}), ({'a', 'b', 'c'}, {'c'}, {'a', 'b'})])
    def test_check_difference_method(self, a, b, dif):
        assert a.difference(b) == dif

    def test_check_intersection_method(self):
        a = {1, 2, 3, 4}
        c = {4, 5, 6}
        assert a.intersection(c) == {4}

    def test_check_union_method(self):
        b = {1, 2, 'f'}
        d = {'d', 'f', 3}
        assert len(b.union(d)) == len(b | d) == 5

    def test_check_pop_method(self):
        r = {'w', 'r', 't'}
        assert len(r.pop()) == len(r) - 1

    def test_check_remove_method(self):
        f_set = {1, 4, 6, 7, 9}
        f_set.remove(4)
        assert 4 not in f_set


