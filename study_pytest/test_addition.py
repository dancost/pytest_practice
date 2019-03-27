import pytest


# param tests using pytest parametrize
@pytest.mark.parametrize("input1, input2, output", [(5,5,10),(5,3,12)])
def test_add(input1, input2, output):
    assert input1 + input2 == output, "fail; reason: {} + {} does not equal {}".format(input1, input2, output)
