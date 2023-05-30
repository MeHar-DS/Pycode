import pytest

# scope has values domain of  - session function
@pytest.fixture(scope = "session", autouse=False)  # Setting autouse to True ensures fixtures are executed prior to every test
def tcsetup():
    print("Launch browser")
    print("Login")
    print("Browse Products")
    yield   #  This is the teardown
    print("Logoff")
    print("Close Browser")