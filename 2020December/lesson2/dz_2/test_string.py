from pytest import mark


class StringMethodsTests:

    @mark.base
    def test_string_isalpha(self, string_abc):
        """Returns True if all characters in the string are in the alphabet"""
        assert string_abc.isalpha()

    @mark.base
    def test_string_isdigit(self, string_123):
        """Returns True if all characters in the string are digits"""
        assert string_123.isdigit()

    @mark.base
    def test_string_lower(self, string_ABC, string_abc):
        """Converts a string into lower case"""
        assert string_ABC.lower() == string_abc

    @mark.base
    def test_string_upper(self, string_abc, string_ABC):
        """Converts a string into upper case"""
        assert string_abc.upper() == string_ABC

    @mark.advance
    @mark.parametrize("pattern, index", [('a', 0), ('b', 1), ('c', 2)])
    def test_string_index(self, string_abc, pattern, index):
        """Searches the string for a specified value and returns the position of where it was found"""
        assert string_abc.index(pattern) == index
