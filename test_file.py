import pytest

@pytest.mark.sanity
def test_username(setup):
    print("hello")

@pytest.mark.regression
def test_password(setup):
    print("password")