import pytest

@pytest.fixture(params=[1,2,3]) #specify parameters
def setup(request):
    retVal=request.param #set return value to the parameter
    print("\nSetup. retVal={}".format(retVal))
    return retVal
def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True