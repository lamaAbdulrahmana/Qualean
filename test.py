import subprocess
import sys
import pytest
import Qualean
from Qualean import qualean
from decimal import Decimal
import time
import os.path
import re
import inspect 
import random
random.seed(10)
import math

README_CONTENT_CHECK_FOR = [
'__and__',
'__or__',
'__repr__',
'__str__',
'__add__',
'__eq__',
'__float__',
'__ge__',
'__gt__',
'__invert__',
'__le__',
'__lt__',
'__mul__',
'__sqrt__',
'__bool__'
]

def test_qualean_values():
    r = qualean (3)

def test_bankers_rounding ():
    q = qualean (1)
    x = str (q._qualean_num)
    x = x.split ('.')[1]
    assert len (x) == 10, x + " 10 decimal places not present"

def test_float_conversion ():
    q = qualean (1)
    x = float (q)
    assert type (x) == type (float ()), "unable to convert to float"


def test_one_million_qs_add ():
    x = 0
    for i in range (1000000):
        x = qualean (random.randint(-1, 1)) + x
    assert math.isclose (x, 0, rel_tol = 1), str (x) + " not nearing to 0"

def test_one_million_qs_mul():
    x = 1
    for i in range (1000000):
        x = qualean (random.randint(-1, 1)) * x
    assert math.isclose (x, 0), "not nearing to 0"


def test_bool_True():
    q1 = qualean (1)
    assert bool (q1) == True, "bool True operator not working"

def test_and_False ():
    q1 = qualean (0)
    q2 = 0
    assert (bool (q1) and q2) == False, "and False not working" 

def test_and_True ():
    q1 = qualean (1)
    q2 = qualean (-1)
    assert (bool (q1) and bool (q2)) == True, "and True not working" 

def test_or_True ():
    q1 = qualean (1)
    q2 = 0
    assert (bool (q1) or q2) == True, "or True not working" 

def test_invert ():
    q1 = qualean (1)
    y = q1._qualean_num
    ~q1
    x = q1._qualean_num
    assert x + y == 0, "Invert not working"

def test_eq ():
    q = qualean (1)
    assert q == q, "equality function not working"

def test_ge ():
    q1 = qualean (1)
    q2 = qualean (-1)
    x1 = q1._qualean_num
    x2 = q2._qualean_num
    if x1 >= x2:
        assert q1 >= q2, "greater than equal to not working"
    else:
        assert q2 >= q1, "greater than equal to not working"

def test_lt():
    q1 = qualean (1)
    q2 = qualean (-1)
    x1 = q1._qualean_num
    x2 = q2._qualean_num
    if x1 < x2:
        assert q1 < q2, "less than not working"
    else:
        assert q2 < q1, "less than not working"

if __name__ ==  '__main__':
    test_clear_memory()