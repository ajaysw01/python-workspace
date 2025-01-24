import sys
from app.sample import add
import pytest

@pytest.mark.skip(reason="wanna skip myself")
def test_add_num() : 
    assert add(1,2) == 3

@pytest.mark.skipif(sys.version_info > (3, 7), reason="use latest version")
def test_add_str() : 
    assert add("ab","cd") == "abcd"

# u know it gonna throw exception but we wanna ignore
@pytest.mark.xfail(sys.platform =="win32",reason="dont run on windows use ubuntu")
def test_add_list() : 
    assert add([1],[2]) == [1,2]
    raise Exception()

