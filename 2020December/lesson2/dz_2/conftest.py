from pytest import fixture, mark
import time


@fixture(scope="session")
def set_time():
    start_date = time.time()
    yield
    last_date = time.time()
    print(last_date - start_date)


@fixture(scope="function")
def empty_list():
    return []


@fixture(scope="function")
def list_123_int():
    return [1, 2, 3]


@fixture(scope="function")
def dict_123_str_to_int():
    return {
        "one": 1,
        "two": 2,
        "three": 3
    }


@fixture(scope="function")
def set_123_int():
    return {1, 2, 3}


@fixture(scope="function")
def set_345_int():
    return {3, 4, 5}


@fixture(scope="function")
def string_123():
    return "123"


@fixture(scope="function")
def string_abc():
    return "abc"


@fixture(scope="function")
def string_ABC():
    return "ABC"


@fixture(params=range(3))
def range_to_2(request):
    return request.param


@fixture(params=[(1, {2, 3}), (2, {1, 3}), (3, {1, 2})])
def set_check(request):
    return request.param
