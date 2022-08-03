
from ipchecker.main import check_for_conflicts

    
def test_check_for_conflicts():
    assert check_for_conflicts() != '0'
