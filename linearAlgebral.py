# -*- coding: iso-8859-15 -*-

from __future__ import division # want 3 / 2 == 1.5
import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplotimport numpy as np
from collections import defaultdict, Counter
from functools import partial

import numpy as np

# 
# functions for working with vectors
#

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def scalar_multiply_np(c, v):
    return c * np.array(v)

def runtime(f):
    from datetime import datetime 
    start_time = datetime.now() 
    data = f
    time_elapsed = datetime.now() - start_time 
    print('{}'.format(time_elapsed), data)

if __name__ == "__main__":
    v = [5, 6, 7, 8]
    scalar = 3

    runtime(scalar_multiply(scalar, v))
    runtime(scalar_multiply_np(scalar, v))
