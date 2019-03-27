import pytest


@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    # an error message will be displayed when assertions fail
    assert x == y, 'test failed because x = {} and y = {}'.format(x, y)


@pytest.mark.set2
def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"

