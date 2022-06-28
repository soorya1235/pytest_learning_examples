import pytest
@pytest.mark.usefixtures("setup")

class test():

    def test_test1(self):
        print("test1")

    def test_test2(self):
        print("test2")

    def test_test3(self):
        print("test3")

    def test_test4(self):
        print("test4")