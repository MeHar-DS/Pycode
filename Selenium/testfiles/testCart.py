import pytest


@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    print("Browse Products")
    yield   #  This is the teardown
    print("Logoff")
    print("Close Browser")

def testAddItemToCart(setup):  # Providng the fixture method name will make the setup method as a pre-requisite
    print("Add Item Successful")

def testRemoveItemFromCart(setup):
    print("Remove Item Successful")
