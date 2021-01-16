import pytest


@pytest.mark.xfail()
@pytest.mark.regress
@pytest.mark.usefixtures('set_time_session','set_time')
@pytest.mark.parametrize("test_a, test_b", [(1, 2), (2, 3), (4, 1)])
def test_firsts(test_a, test_b, start_num):
    # test_a = 2
    # b = 3
    assert (test_a + test_b) * 10 == start_num[0] + start_num[1]

