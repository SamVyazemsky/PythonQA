import pytest

@pytest.mark.smoke
@pytest.mark.xfail(reason="cause look at bug #123")
def test_firsts():
    a = 2
    b = 3
    assert "abc" == "abc"
