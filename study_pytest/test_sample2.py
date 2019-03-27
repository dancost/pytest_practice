import pytest


# pytest markers allow us to run different sets of tests, based on marker names
@pytest.mark.set1
def test_file2_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, 'test failed because x = {} and y = {}'.format(x, y)


@pytest.mark.set1
def test_file2_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"

