import pytest

@pytest.fixture()
def setup1():
    print("\nSetup")
    yield
    print("\nTeardown")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown 1")
    def teardown_b():
        print("\nTeardown 2")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test1")
    assert True

def test2(setup2):
    print("Executing test2")
    assert True