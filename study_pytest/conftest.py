import pytest


# pytest fixture function - this will be called before any test that uses it as an argument
@pytest.fixture
def supply_AA_BB_CC():
    aa = 25
    bb = 35
    cc = 45
    return[aa, bb, cc]