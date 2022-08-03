""" Meh """
from ipchecker.functions import check_conflicts

def test_check_conflicts():
    """ Meh """
    # check for conflict
    assert check_conflicts(["192.168.0.0/20","192.168.1.0/22"]) == {"result": "overlap"}
    # check for co conflict
    assert check_conflicts(["192.168.0.0/28","192.168.1.0/24"]) == {"result": "ok"}