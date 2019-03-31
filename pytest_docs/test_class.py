class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        # hasattr would check if getattr() returns AttributeError
        # and return True or False
        assert hasattr(x, 'check')
        
