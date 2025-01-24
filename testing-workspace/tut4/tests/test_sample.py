from app.sample import add
import pytest
# def test_add_num() : 
#     assert add(1,2) == 3

# def test_add_str() : 
#     assert add("ab","cd") == "abcd"

# def test_add_list() : 
#     assert ([2],[3]) == [2,3]


# parameterized teste
@pytest.mark.parametrize("a,b,c",[(1,2,3),("A","b","Ab"),([1,2],[3],[1,2,3])]
                         , ids=["num","str","list"])
def test_add(a,b,c) : 
    assert add(a,b) == c
    
