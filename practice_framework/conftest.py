import pytest

#fixture that will supply all base url for all test methods

@pytest.fixture
def supply_url():
    return "https://reqres.in/api"
