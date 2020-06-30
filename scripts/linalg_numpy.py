#!/bin/python3

import numpy as np


# Do not change these variables
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

# Q1: record the dimensions of A, B, C, D, u, v respectively in the dict below. 
#     Do not type the answers, make python do the work

dimensions = {
    'A': A.shape,
    'B': B.shape,
    'C': C.shape,
    'D': D.shape,
    'u': u.shape,
    'v': v.shape
}

# Q2: vector operations
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
alpha = 6
from scipy import linalg

u_plus_v = u+v            # u+v
u_minus_v = u-v         # u-v
alpha_times_u = alpha*u      # alpha * u, alpha = 6
u_dot_v = np.dot(u,v)           # u . v
norm_u = np.linalg.norm(u)             # ||u|| 


# Q3: compute the following and assign to variables below:
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work

A_plus_C = None             # A + C
A_minus_Ctranspose = A - C.transpose()    # A - C.T
Ctranspose_plus_3D = C.transpose() + (3*D)    # C.T + 3*D
B_times_A = np.dot(B,A)            # B*A
B_times_Atranspose = None   # B*A.T

# Q4: (bonus)
B_times_C = None            # B*C
C_times_B = np.dot(C,B)            # C*B
B_exp_4 = np.linalg.matrix_power(B,4)           # B^4
A_times_Atranspose = np.dot(A,A.transpose())   # A*A.T
Dtranspose_times_D = np.dot(D.transpose(),D)    # D.T*D