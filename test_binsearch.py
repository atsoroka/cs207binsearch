from pytest import raises
from binsearch import binary_search
import numpy as np

def test_BS():
	input = list(range(10))
    assert binary_search(input,5) == 5

def decimal_BS():
	input = list(range(10))
    assert binary_search(input,4.5) == -1

def exceeds_BS():
	input = list(range(10))
    assert binary_search(input,10) == -1

def single_BS():
    assert binary_search([5], 5) == 0

def singleNot_BS():
    assert binary_search([5], 4) == -1

def wInf_BS():
    assert binary_search([1,2,np.inf], 2) == 1

def wInf2_BS():
    assert binary_search([1,2,np.inf], np.inf) == 2

def  leftRight_BS():
	input = list(range(10))
	assert binary_search(input, 5, 1,3) ==  -1

def  leftRight2_BS():
	input = list(range(10))
	assert binary_search(input, 2, 1,3) == 2

def crossLeftRight_BS():
	input = list(range(10))
	assert = binary_search(input, 2, 3, 1) == -1

def sameLeftRight_BS():
	input = list(range(10))
	assert binary_search(input, 2, 2, 2) == 2

def sameLeftRight2_BS():
	binary_search(input, 5, 2, 2) == -1



