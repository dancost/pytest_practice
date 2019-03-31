import pytest

'''
# param tests using pytest parametrize
@pytest.mark.parametrize("input1, input2, output", [(5, 5, 10), (5, 3, 12)])
# test method accepts three arguments: input1, input2 and output
def test_add(input1, input2, output):
    assert input1 + input2 == output, "fail; reason: {} + {} does not equal {}".format(input1, input2, output)
'''

@pytest.mark.skip
def test_add_1():
    assert 100+200 == 400, "failed"

@pytest.mark.skip
def test_add_2():
    assert 100 + 200 == 300, "failed"

@pytest.mark.xfail
def test_add_3():
    assert 15+13 == 28, "failed"

@pytest.mark.xfail
def test_add_4():
    assert 15+13 == 100, "fail"

#@pytest.mark.xfail
def test_add_5():
    assert 3+2 == 5, "failed"

#@pytest.mark.xfail
def test_add_6():
    assert 3+2 == 6, "falied"
