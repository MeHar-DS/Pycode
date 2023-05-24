import pytest


def testLogin():
    print("Login Successful")

def testLogoff():
    print("Logoff Successful")

@pytest.mark.sanity
def testCalculation():
    assert 2+2 == 4

@pytest.mark.xfail
def testexpectedFaildemo():
    assert 2+2 == 5

@pyest.mark.skip
def skiptestdemo():
    print("this will be skipped")