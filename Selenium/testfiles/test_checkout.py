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

# def test_login(setup):
#     print("Login Successful")

# Commented the above code to demonstrate the conftest behavior of tcsetup in conftest file


def test_login_using_conftest(tcsetup):
    print("Login Successful")


def test_logoff():
    print("Logoff Successful")


def test_calculation():
    assert 2+2 == 4

