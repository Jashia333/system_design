import pytest
from token_bucket import my_bucket

def test_intial():
    bucket=my_bucket(capacity=5, drop_rate=2)
    assert bucket.allow_req()==True

