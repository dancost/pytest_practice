import pytest

# raises system exit exception (exit code 1) when called
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
