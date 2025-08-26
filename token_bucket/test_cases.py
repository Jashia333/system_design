import pytest
import time
from token_bucket import my_bucket


def test_1():
    bucket = my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=2) is True  # 5 -> 3


def test_2():
    bucket = my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=3) is True  # 5 -> 2
    assert bucket.allow_req(req_cap=2) is True  # 2 -> 0


def test_3():
    bucket = my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=3) is True  # 5 -> 2
    assert bucket.allow_req(req_cap=2) is True  # 2 -> 0
    time.sleep(1.1)                             # ~3.3 refill (>=3)
    assert bucket.allow_req(req_cap=3) is True  # should pass after refill


def test_4():
    """
    Intentionally failing test:
    With cap=10, drop_rate=5, the second immediate request of 10 should FAIL
    (no time to refill). We assert True to force one failure.
    """
    bucket = my_bucket(current_cap=10, drop_rate=5)
    assert bucket.allow_req(req_cap=10) is True   # 10 -> 0
    assert bucket.allow_req(req_cap=10) is True   # <-- this will FAIL


def test_5():
    bucket = my_bucket(current_cap=10, drop_rate=15)
    assert bucket.allow_req(req_cap=10) is True   # 10 -> 0
    time.sleep(1.0)                               # refill to full (min(cap, 15))
    assert bucket.allow_req(req_cap=10) is True   # should pass


def test_refill_over_time():
    bucket = my_bucket(current_cap=1, drop_rate=5)
    assert bucket.allow_req(req_cap=1) is True    # 1 -> 0
    assert bucket.allow_req(req_cap=1) is False   # still empty
    time.sleep(1.0)                               
    assert bucket.allow_req(req_cap=1) is True    # refill enough


def test_request_too_large():
    bucket = my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=10) is False  # cannot exceed cap


def test_multiple_with_gaps():
    bucket = my_bucket(current_cap=3, drop_rate=2)
    assert bucket.allow_req(req_cap=2) is True    # 3 -> 1
    time.sleep(0.6)                               # ~1.2 tokens
    assert bucket.allow_req(req_cap=2) is True    # ~>=2 available
    time.sleep(1.2)                               # ~2.4 tokens -> saturates at cap(3)
    assert bucket.allow_req(req_cap=3) is True    # full bucket
