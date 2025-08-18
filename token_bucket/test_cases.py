import pytest
from token_bucket import my_bucket

def test_1():
    bucket=my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=2)==True

def test_2():
    bucket=my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=3)==True
    assert bucket.allow_req(req_cap=2)==True
    #assert bucket.allow_req(req_cap=3)==True

def test_3():
    bucket=my_bucket(current_cap=5, drop_rate=3)
    assert bucket.allow_req(req_cap=3)==True
    assert bucket.allow_req(req_cap=2)==True
    assert bucket.allow_req(req_cap=3)==True

def test_4():
    bucket=my_bucket(current_cap=10, drop_rate=5)
    assert bucket.allow_req(req_cap=10)==True
    assert bucket.allow_req(req_cap=10)==True

def test_5():
    bucket=my_bucket(current_cap=10, drop_rate=15)
    assert bucket.allow_req(req_cap=10)==True
    assert bucket.allow_req(req_cap=10)==True
    #assert bucket.allow_req(req_cap=10)==True
    

