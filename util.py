# -*- coding: utf-8 -*-
from numpy import linalg as LA
import numpy as np
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%s; Время вычисления: %f секунды' % (result, te-ts)
        return result

    return timed

@timeit
def calculate_1a(v1, v2, x, y):
	f  = 1 - v1**2 - v2 ** 2 + v1 * v2
	_f = -1 * f

	a1 = np.array([
		[1,  2*v1 - v2, 2*v2 - v1, _f,    0,    	  0         ], 
		[v1, 1 + v2, 	v1 - v2,   0,	  _f, 	      0         ],
		[v2, v1, 	 	1 - v2,    0,     0,    	  _f        ],
		[f,  0,			0,         1 - f, 2*v1 - v2,  2*v2 - v1 ],
		[0,  f,         0,         v1,    1 + v2 - f, v1 - v2   ],
		[0,  0,			f, 		   v2,	  v1,         1 - v2 - f]        
	]) 

	a2_inv = LA.inv(np.array([
		[1-f, 2*v1-v2, 2*v2-v1, f,  0,		 0		],
		[v1,  1-f+v2,  v1-v2,   0,  f, 		 0		],
		[v2,  v1,      1-f-v2,  0,  0, 		 f 	    ],
		[_f,  0,       0, 	    1,  2*v1-v2, 2*v2-v1],
		[0,   _f,      0, 		v1, 1+v2,    v1-v2  ],
		[0,   0, 	   _f,		v2, v1,      1-v2   ]
	        
	])) #генерируем a2 и сразу инвертируем 

	a3 = np.dot(a1, a2_inv) #перемножаем матрицы

	#берём первый столбец
	a11, a21, a31, a41, a51, a61 = a3[0][0], a3[1][0], a3[2][0], a3[3][0], a3[4][0], a3[5][0]

	#вычисляем коэффициент beta
	beta = a11 + y*a21 + (y**2-2)*a31 + x*a41 + y*x*a51 + x*(y**2-2)*a61

	return "Коэффициент бета: %f" % beta

@timeit
def calculate_1b(u1, u2, u3, u1_, u2_, u3_):

	a1 = np.array([
		[u1+1, 2*u2-u3, 2*u3-u2], 
       	[u2,   u1+u3+1, u2-u3  ],
       	[u3,   u2,      u1+1-u3]
	]) 

	a2_inv = LA.inv(np.array([
		[u1_, 2*u2_-u3_, 2*u3_-u2_],
		[u2_, u1_+u3_,   u2_-u3_  ],
		[u3_, u2_,       u1_-u3_  ]	        
	])) #генерируем a2 и сразу инвертируем 

	a3 = np.dot(a1, a2_inv) #перемножаем матрицы

	#берём первый столбец
	a11, a21, a31 = a3[0][0], a3[1][0], a3[2][0]

	return "Кортеж: (%f, %f)" % (a21/float(a11), a31/float(a11))