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

# this isn't right if you don't from __future__ import division
def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def runtime(f):
    from datetime import datetime 
    start_time = datetime.now() 
    data = f
    time_elapsed = datetime.now() - start_time 
    print('{}'.format(time_elapsed), data)

if __name__ == "__main__":
    v = [1,2,3,4]
    w = [-4,-3,-2,-1]

    runtime(vector_mean([v,v,v,v]))
    runtime(np.mean([v,v,v,v], axis=0))
