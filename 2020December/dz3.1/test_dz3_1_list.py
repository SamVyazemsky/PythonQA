import pytest


class TestList:
    @pytest.mark.parametrize("ind, elem", [(0, 3), (1, 2), (2, 1)])
    def test_check_pop_method(self, ind, elem):
        lst = [3, 2, 1]
        assert lst.index(elem) == ind

    def test_check_copy_method(self):
        w = [4, 6, 8, 0]
        v = w.copy()
        assert v == w[:] == w

    def test_check_sort_method(self):
        q = [3, 7, -5, -1, 9, 0]
        m = max(q)
        q.sort()
        assert q[-1] == m

    def test_check_remove_and_count_methods(self):
        ls = [1, 2, 3]
        ls.remove(2)
        assert ls.count(2) == 0

    def test_check_clear_method(self):
        r = [3, 5, 6]
        r.clear()
        assert r == []

    # Два дополнительных теста на функцию zip

    a = [1, 2, 3, 4]
    b = [10, 20, 30]
    c = ['a', 'b', 'c', 'd']

    def test_check_length_of_list_after_zip(self):
        min_len = min(len(self.a), len(self.b))
        assert len(list(zip(self.a, self.b))) == min_len

    def test_check_valid_unpacking_after_zip(self):
        rez = zip(self.a, self.c)
        col1, col2 = zip(*rez)
        assert list(col1) == self.a
        assert list(col2) == self.c

