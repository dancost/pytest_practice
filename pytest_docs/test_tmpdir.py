
# using tmpdir in the function signature will make pytest create tempfolders
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0
