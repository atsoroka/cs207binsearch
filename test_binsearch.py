
### Anthony Soroka HW 4 CS 207

from pytest import raises
from binsearch import binary_search
import numpy as np
import random

# baseline test that binary search can find value in sorted list
def test_BS():
	myInput = list(range(10))
	assert binary_search(myInput,5) == 5

# Index returned is less than length of the input
def test_BS_index():
	myInput = list(range(10))
	mySearch = random.randrange(0,10)
	index = binary_search(myInput,mySearch)
	assert index < len(myInput)

# baseline test that binary search can find value in a set
def test_BS_set():
	myInput = set(list(range(10)))
	with raises(TypeError):
		binary_search(myInput,5)

# baseline test that binary search can find value in sorted NumpyArray
def test_BS_np():
	myInput = np.array(list(range(10)))
	assert binary_search(myInput,5) == 5
	
#if value not in list, return -1
def test_decimal_BS():
	myInput = list(range(10))
	assert binary_search(myInput,4.5) == -1

#if needle is great than max value in list, return -1
def test_exceeds_BS():
	myInput = list(range(10))
	assert binary_search(myInput,10) == -1

#single value list runs as expected
def test_single_BS():
	assert binary_search([5], 5) == 0

#single value list can return -1
def test_singleNot_BS():
	assert binary_search([5], 4) == -1

#if 'nan' is passed, user has violated agreement as NAN isn't really sortable
def test_Nan_BS():
	nan = [float('nan'),1] 
	assert binary_search(nan,1) == 0

#if 'nan' is passed, user has violated agreement as NAN isn't really sortable
def test_Nan2_BS():
	nan = [np.nan,1,2,3,4,5] 
	assert binary_search(nan,1) == 0

#if 'nan' is passed, user has violated agreement as NAN isn't really sortable
def test_Nan3_BS():
	nan = [np.nan,1,2,3,4,5] 
	assert binary_search(nan,2) == 2

#if np.inf is list, can still locate needle
def test_wInf_BS():
	assert binary_search([1,2,np.inf], 2) == 1

#if np.inf is list, can still locate needle of np.inf
def test_wInf2_BS():
	assert binary_search([1,2,np.inf], np.inf) == 2

# left right values set, function still runs, value not found
def  test_leftRight_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 5, 1,3) ==  -1

# left right values set, function still runs, value found
def  test_leftRight2_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 2, 1,3) == 2

# left right values cross, function returns -1
def crossLeftRight_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 2, 3, 1) == -1

# left right values set to same value, function still runs, value found
def test_sameLeftRight_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 2, 2, 2) == 2

# left right values set to same value, function still runs, value not found
def test_sameLeftRight2_BS():
	myInput = list(range(10))
	assert binary_search(myInput, 5, 2, 2) == -1

# Binary search works on character list
def test_char_BS():
	myInput = ['a','b','c']
	assert binary_search(myInput,'b') == 1

# Binary search works on string list
def test_string_BS():
	myInput = ['Anthony','Betty','Charlie']
	assert binary_search(myInput,'Charlie') == 2

# Binary search works on string
def test_string2_BS():
	myInput = "abcdefg"
	assert binary_search(myInput,'d') == 3

# Binary search works on  float list
def char_BS():
	myInput = [1.1,1.2,1.3]
	assert binary_search(myInput,1.4) == 1

#When there are a multiple entries of the needle, binary search will
# return a valid index, but the index it returns depends on each scenario
def test_multipleTimes():
	myInput = [5,5,5]
	assert binary_search(myInput,5) == 1

def test_multipleTimes2():
	myInput = [5,5,5,5,5]
	assert binary_search(myInput,5) == 2

def test_multipleTimes3():
	myInput = [1,1,2,3,4]
	assert binary_search(myInput,1) == 0

def test_multipleTimes4():
	myInput = [1,2,3,4,4]
	assert binary_search(myInput,4) == 3

#Neg Inf in list, still can locate neg inf
def test_negInf_BS():
	assert binary_search([-np.inf,1,2,np.inf], -np.inf) == 0

# Negative Left Index still runs and returns as normal
def test_negativeIndex():
	myInput = list(range(10))
	assert binary_search(myInput,2,-5,5) == 2

# Inf as an  Index returns an error
def test_InfIndex():
	myInput = list(range(10))
	with raises(TypeError):
		binary_search(myInput, 2, 1,np.inf)

#Int Inf as an index, returns an error
def test_IntInfIndex():
	myInput = list(range(10))
	with raises(OverflowError):
		binary_search(myInput, 2, 1,int(np.inf))

#Right surpasses index, returns an error
def test_ExceedIndex():
	myInput = list(range(10))
	with raises(IndexError):
		binary_search(myInput, 2, 1,50)

#da_Array is not an array
def test_non_array():
	myInput = 12345
	with raises(TypeError):
		binary_search(myInput, 5)

#da_Array is not an array
def test_non_array2():
	myInput = 12345
	with raises(TypeError):
		binary_search(myInput, myInput)

#da_array and needle are the same array
def test_needle_array():
	myInput = list(range(10))
	with raises(TypeError):
		binary_search(myInput, myInput)

#da_array is an array of array
def test_arrayofarray():
	myInput = [[1],[2],[3],[4],[5]]
	assert binary_search(myInput,[3]) == 2

#da_array is a dictionary
def test_dictionary():
	myInput = {'A' : 'a', 'B' : 'b', 'C': 'c'}
	with raises(KeyError):
		binary_search(myInput, myInput['A'])

#da_array is not sorted, user broke agreement
def test_notSorted():
	myInput = [6,5,4]
	assert binary_search(myInput,4) == -1



