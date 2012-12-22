# -*- coding: utf-8 -*-
from numpy import linalg as LA
from copy import deepcopy as copy


a11, a12, a13, a14, a15, a16 = 1,2,3,4,5,6
a21, a22, a23, a24, a25, a26 = 6,5,4,3,2,1
a31, a32, a33, a34, a35, a36 = 1,2,3,4,5,7
a41, a42, a43, a44, a45, a46 = 1,0,3,4,1,6
a51, a52, a53, a54, a55, a56 = 1,2,9,4,5,6
a61, a62, a63, a64, a65, a66 = 1,3,3,8,5,6

A = [
	[a11, a12, a13, a14, a15, a16], 
	[a21, a22, a23, a24, a25, a26],
	[a31, a32, a33, a34, a35, a36],
	[a41, a42, a43, a44, a45, a46],
	[a51, a52, a53, a54, a55, a56],
	[a61, a62, a63, a64, a65, a66]        
]

def m(i, j, A):
	M = copy(A)

	for _i in range(6):
		for _j in range(6):
			if i == _i or j == _j:
				M[_i][_j] = None

	return filter(lambda x: len(x) > 0, map(lambda x: filter(lambda x: x is not None, x), M))

S = [
	[None, None, None, None, None, None],
	[None, None, None, None, None, None],
	[None, None, None, None, None, None],
	[None, None, None, None, None, None],
	[None, None, None, None, None, None],
	[None, None, None, None, None, None]
]

for i in range(6):
	for j in range(6):
		S[i][j] = int(round((-1)**(i + 1 + j + 1) * LA.det(m(i, j, A))))

print "Матрица S => %s" % S
