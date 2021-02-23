import numpy as np
"""
quantum state defined by n*1 vector
>>> basis(2,3)
array([[0.+0.j],
       [0.+0.j],
       [1.+0.j]])
"""
def basis(d,n):
    st=np.zeros([n,1],dtype=('complex128'))
    st[d,0]=1
    return st


"""
ket is allias for basis 
"""
def ket(d,n):
    kt=basis(d,n)
    return kt


"""
bra is conjugate transpose for ket
which is 1*n matrix
"""
def bra(d,n):
    br=basis(d,n).conj().T
    return br
"""
projection operator
n><m
>>> projection(0,1,2)
array([[0.+0.j, 1.+0.j],
       [0.+0.j, 0.+0.j]])
"""

def projection(n,m,d):
    pr=ket(n,d)@bra(m,d)
    return pr




print(basis(1,3))
