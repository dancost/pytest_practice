
# build-in fixture tmp_path creates a temp path for the duration of
# the test, if it is used in the function signature - simial to
# tmpdir
def test_path(tmp_path):
    print(tmp_path)
    assert 0
