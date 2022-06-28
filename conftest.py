import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataload():
    return ["soorya","saravanan"]

@pytest.fixture(params=[("chrome","soorya","saravanan"),"firefox","IE"])
def data_parameter(request):
    return request.param
