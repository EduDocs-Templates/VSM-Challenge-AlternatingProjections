import numpy as np
from scipy.linalg import inv, svd
from tqdm import tqdm_notebook as tqdm

### Helper functions

# Compute null space
def null_space(A, rcond=None):
    """
    Compute null spavce of matrix XProjection on half space defined by {v| <v,w> = c}
    Arguments:
        A {numpy.ndarray} -- matrix whose null space is desired
        rcond {float} -- intercept
    Returns:
        Q {numpy.ndarray} -- matrix whose (rows?) span null space of A
    """
    u, s, vh = svd(A, full_matrices=True)
    M, N = u.shape[0], vh.shape[1]
    if rcond is None:
        rcond = np.finfo(s.dtype).eps * max(M, N)
    tol = np.amax(s) * rcond
    num = np.sum(s > tol, dtype=int)
    Q = vh[num:,:].T.conj()
    return Q

### End Helper Functions

# Exercise 1: Alternating projection for subspaces
def altproj(A, B, v0, n):
    """
    Arguments:
        A {numpy.ndarray} -- matrix whose columns form basis for subspace U
        B {numpy.ndarray} -- matrix whose columns form baiss for subspace W
        v0 {numpy.ndarray} -- initialization vector
        n {int} -- number of sweeps for alternating projection
    Returns:
        v {numpy.ndarray} -- the output after 2n steps of alternating projection
        err {numpy.ndarray} -- the error after each full pass
    """
    
    ### Add code here
    
    return v, err

# Exercise 2: Kaczmarz algorithm for solving linear systems
def kaczmarz(A, b, I):
    """
    Arguments:
        A {numpy.ndarray} -- matrix defines the LHS of linear equation
        b {numpy.ndarray} -- vector defines the RHS of linear equation
        I {int} -- number of full passes through the Kaczmarz algorithm
    Returns:
        X {numpy.ndarray} -- the output of all I full passes
        err {numpy.ndarray} -- the error after each full pass
    """
    
    ### Add code here

    return X, err

# Exercise 4: Alternating projection to satisfy linear inequalities
def lp_altproj(A, b, I, s=1):
    """
    Find a feasible solution for A v >= b using alternating projection
    starting from v0 = 0
    Arguments:
        A {numpy.ndarray} -- matrix defines the LHS of linear equation
        b {numpy.ndarray} -- vector defines the RHS of linear equation
        I {int} -- number of full passes through the alternating projection
        s {numpy.float} -- step size of projection (defaults to 1)
    Returns:
        v {numpy.ndarray} -- the output after I full passes
        err {numpy.ndarray} -- the error after each full pass
    """
    
    # Add code here
    
    return v, err