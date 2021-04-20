import pytest
@pytest.fixture(autouse="true")
def myfixture():
    print("执⾏myfixture")