import pytest

from pytesttesting.BaseClass import BaseClass
from pytesttesting.testclass import testclass


@pytest.mark.usefixtures("dataload")
class Testexample2(BaseClass):

    def test_print(self,dataload):
        log = self.getLogger()
        log.info(dataload)

