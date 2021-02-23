import numpy as np
def basis(d,n):
    st=np.zeros([n,1],dtype=('complex128'))
    st[d,0]=1
    return st
def ket(d,n):
    kt=basis(d,n)
    return kt
def bra(d,n):
    br=basis(d,n).conj().T
    return br
def projection(n1,n2,d):
    pr=ket(n1,d)@bra(n2,d)
    return pr




print(projection(0,1,3))
