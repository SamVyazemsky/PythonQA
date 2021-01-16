import pytest


class TestString:
    @pytest.mark.parametrize("letter, col", [('h', 1), ('e', 1), ('l', 3)])
    def test_count_of_letters(self, letter, col):
        string = 'hello, world!'
        assert string.count(letter) == col

    def test_check_upper_method(self):
        assert 'hello'.upper() == 'HELLO'

    def test_check_ljust_method(self):
        string = "I am"
        string = string.ljust(10, '_')
        assert len(string) == 10

    def test_check_replace_method(self):
        string = 'frenzy'
        string = string.replace('z', '-')
        assert string.find('z') == -1

    def test_check_isdigit_method(self):
        string = '12234325'
        assert string.isdigit()

