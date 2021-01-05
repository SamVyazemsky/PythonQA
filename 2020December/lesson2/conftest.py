import pytest
from datetime import datetime


@pytest.fixture(scope="session")
def set_time_session():
    start_date = datetime.now()
    yield
    last_date = datetime.now()
    print(last_date - start_date)


@pytest.fixture(scope="function")
def set_time():
    start_date = datetime.now()
    yield
    last_date = datetime.now()
    print(last_date - start_date)


@pytest.fixture(params=(10, 20, 30, 40, 50))
def stop_num(request):
    return request.param


@pytest.fixture(params=(1, 2, 3, 4, 5))
def start_num(request, stop_num):
    return request.param, stop_num
