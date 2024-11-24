import pytest

@pytest.fixture(scope="module",autouse=True)
def setup1():
    print("\nSetup Module 2")

@pytest.fixture(scope="class",autouse=True)
def setup2():
    print("\nSetup Class")

@pytest.fixture(scope="function",autouse=True)
def setup3():
    print("\nSetup Function 2")

class TestClass:
    def test3(self):
        print("Executing test3")
        assert True

    def test4(self):
        print("Executing test4")
        assert True