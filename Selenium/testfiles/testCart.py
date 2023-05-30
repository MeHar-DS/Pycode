# import pytest
#
#
# @pytest.fixture()
# def setup():
#     print("Launch browser")
#     print("Login")
#     print("Browse Products")
#     yield   #  This is the teardown
#     print("Logoff")
#     print("Close Browser")
# Commented the above code to demonstrate the conftest behavior of tcsetup in conftest file

# def test_add_item_to_cart(setup):  # Providing the fixture method name will make the setup method as a pre-requisite
#     print("Add Item Successful")


def test_add_item_to_cart(tcsetup):  # Providing conftest behavior by grouping commonly used function in conftest file
    print("Add Item Successful")


def test_remove_item_from_cart(setup):   # this fails since setup is not defined conftest is not invoked in this case since setup is explicitly called
    print("Remove Item Successful")
