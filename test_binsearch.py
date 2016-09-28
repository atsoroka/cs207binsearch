
from pytest import raises
from binsearch import binary_search
import numpy as np

def test_BS():
	myInput = list(range(10))
	assert binary_search(myInput,5) == 5

def decimal_BS():
	myInput = list(range(10))
	assert binary_search(myInput,4.5) == -1

def exceeds_BS():
	myInput = list(range(10))
	assert binary_search(myInput,10) == -1

def single_BS():
	assert binary_search([5], 5) == 0

def singleNot_BS():
	assert binary_search([5], 4) == -1

def wInf_BS():
	assert binary_search([1,2,np.inf], 2) == 1

def wInf2_BS():
	assert binary_search([1,2,np.inf], np.inf) == 2

def  leftRight_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 5, 1,3) ==  -1

def  leftRight2_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 2, 1,3) == 2

def crossLeftRight_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 2, 3, 1) == -1

def sameLeftRight_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 2, 2, 2) == 2

def sameLeftRight2_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 5, 2, 2) == -1


# Multiple 
def multipleTimes():
	myInput = [5,5,5]
	assert binary_search(myInput,5) == 1

# Multiple 
def multipleTimes2():
	myInput = [5,5,5,5,5]
	assert binary_search(myInput,5) == 2

# Multiple 
def multipleTimes3():
	myInput = [1,1,2,3,4]
	assert binary_search(myInput,1) == 0

# Multiple 
def multipleTimes4():
	myInput = [1,2,3,4,4]
	assert binary_search(myInput,4) == 3

#Inf in list, still can locate inf
def negInf_BS():
	assert binary_search([-np.inf,1,2,np.inf], -np.inf) == 0

# Negative Index
def negativeIndex():
	myInput = list(range(10))
	assert binary_search(myInput,2,-5,5) == 2

def InfIndex():
	myInput = list(range(10))
	with raises(TypeError):
		binary_search(myInput, 2, 1,np.inf)

def IntInfIndex():
	myInput = list(range(10))
	with raises(OverflowError):
		binary_search(myInput, 2, 1,int(np.inf))

def ExceedIndex():
	myInput = list(range(10))
	with raises(IndexError):
		binary_search(myInput, 2, 1,50)