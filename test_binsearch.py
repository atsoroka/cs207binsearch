from pytest import raises
from binsearch import binary_search

def test_BS():
    assert binary_search(range(10),5) == 5