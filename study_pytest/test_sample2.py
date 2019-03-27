
def test_file2_method1():
    x = 5
    y = 6
    assert x+1 == y, "test failed"
    # an error message will be displayed when assertions fail
    assert x == y, 'test failed because x = {} and y = {}'.format(x, y)


def test_file2_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"

