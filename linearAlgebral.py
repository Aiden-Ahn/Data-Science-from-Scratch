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

def runtime(f):
    from datetime import datetime 
    start_time = datetime.now() 
    data = f
    time_elapsed = datetime.now() - start_time 
    print('{}'.format(time_elapsed), data)

if __name__ == "__main__":
    v = [x for x in range(1, 11,2)]
    w = [y for y in range(11, 21,2)]
    print(v)
    print(w)
    vectors = [v,w,v,w,v,w]
    runtime(vector_sum(vectors))
    runtime(np.sum([v,w,v,w,v,w], axis=0))