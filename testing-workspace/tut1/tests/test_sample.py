from app.sample import add
def test_add_num() : 
    assert add(1,2) == 3

def test_add_str() : 
    assert add("ab","cd") == "abcd"


class TestSample : 
    def test_add_num(self) : 
     assert add(1,2) == 3

    def test_add_str(self) : 
        assert add("ab","cd") == "abcd"