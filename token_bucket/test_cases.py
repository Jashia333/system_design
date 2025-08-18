import pytest
from token_bucket import my_bucket

def test_intial():
    bucket=my_bucket(capacity=5, drop_rate=2)
    assert bucket.allow_req(req_cap=2)==True

def test_intial_2():
    bucket=my_bucket(capacity=5, drop_rate=2)
    assert bucket.allow_req(req_cap=3)==True
    assert bucket.allow_req(req_cap=2)==True
    assert bucket.allow_req(req_cap=3)==True

