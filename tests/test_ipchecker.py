""" Test functions """
from app.functions import check_conflicts, get_ip_set


def test_check_conflicts():
    """ Check for overlapping subnets from check_conflicts function """
    # check for conflict
    assert check_conflicts(["192.168.0.0/20", "192.168.1.0/22"]) == {
        "result": "subnets overlap"
    }
    # check for co conflict
    assert check_conflicts(["192.168.0.0/28", "192.168.1.0/24"]) == {
        "result": "subnets ok"
    }


def test_get_ip_set():
    """Check given subnet returns a subnet"""
    assert "192.168.0.0/28" in (get_ip_set("192.168.0.0/28"))
