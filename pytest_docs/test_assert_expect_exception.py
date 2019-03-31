import pytest


# raises a value error with a custom message when called
def my_func():
    raise ValueError('Exception 123 raised!')

# regex matching can be done when evaluation exceptions with pytest
def test_match():
    with pytest.raises(ValueError, match=r'.*123.*'):
        my_func()
