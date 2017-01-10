from __future__ import absolute_import, division, print_function

import dask.array as da
import dask.dataframe as dd
from multipledispatch import dispatch
import numpy as np
import pandas as pd
from scipy.stats import chi2

@dispatch(np.ndarray)
def sigmoid(x):
    '''Sigmoid function of x.'''
    return 1/(1+np.exp(-x))

@dispatch(da.Array)
def sigmoid(x):
    '''Sigmoid function of x.'''
    return 1/(1+da.exp(-x))

@dispatch(np.ndarray)
def exp(A):
    return np.exp(A)

@dispatch(da.Array)
def exp(A):
    return da.exp(A)

@dispatch(np.ndarray)
def log1p(A):
    return np.log1p(A)

@dispatch(da.Array)
def log1p(A):
    return da.log1p(A)

@dispatch(da.Array,np.ndarray)
def dot(A,B):
    B = da.from_array(B, chunks=A.shape)
    return da.dot(A,B)

@dispatch(np.ndarray,da.Array)
def dot(A,B):
    A = da.from_array(A, chunks=B.shape)
    return da.dot(A,B)

@dispatch(np.ndarray,np.ndarray)
def dot(A,B):
    return np.dot(A,B)

@dispatch(da.Array,da.Array)
def dot(A,B):
    return da.dot(A,B)

@dispatch(np.ndarray)
def sum(A):
    return np.sum(A)

@dispatch(da.Array)
def sum(A):
    return da.sum(A)