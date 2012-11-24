# -*- coding: utf-8 -*-
from numpy import linalg as LA
import numpy as np
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%s;\t Время вычисления: %f секунды\n' % (result, te-ts)
        return result

    return timed

@timeit
def calculate_1a(p, v1, v2):
	f  = (1 - v1**2 - v2 ** 2 + v1 * v2) % p
	_f = -1 * f

	a1 = np.array([
		[1%p,  (2*v1-v2)%p, (2*v2-v1)%p, _f%p,    0%p,    	   0           ], 
		[v1%p, (1+v2)%p, 	(v1-v2)%p,   0,	      _f%p, 	   0           ],
		[v2%p, v1%p, 	 	(1-v2)%p,    0,       0,    	   _f          ],
		[f%p,  0,			0,           (1-f)%p, (2*v1-v2)%p, (2*v2-v1)%p ],
		[0,    f%p,         0,           v1%p,    (1+v2-f)%p,  (v1-v2)%p   ],
		[0,    0,			f%p, 		 v2%p,	  v1%p,        (1-v2-f)%p  ]        
	]) % p

	a2_inv = LA.inv(np.array([
		[(1-f)%p, (2*v1-v2)%p, (2*v2-v1)%p, f%p,  0,		   0		  ],
		[v1%p,    (1-f+v2)%p,  (v1-v2)%p,   0,    f%p, 		   0	      ],
		[v2%p,    v1%p,        (1-f-v2)%p,  0,    0, 		   f%p        ],
		[_f%p,    0,           0, 	        1%p,  (2*v1-v2)%p, (2*v2-v1)%p],
		[0,       _f%p,        0, 		    v1%p, (1+v2)%p,    (v1-v2)%p  ],
		[0,       0, 	       _f%p,		v2%p, v1%p,        (1-v2)%p   ]
	        
	])) % p #генерируем a2 и сразу инвертируем + берём по модулю p

	a3 = np.dot(a1, a2_inv) #перемножаем матрицы

	#берём первый столбец
	a11, a21, a31, a41, a51, a61 = a3[0][0]%p, a3[1][0]%p, a3[2][0]%p, a3[3][0]%p, a3[4][0]%p, a3[5][0]%p

	return "Бета: %i + y*%i + (y**2-2)*%i + x*%i + y*x*%i + x*(y**2-2)*%i" % (a11, a21, a31, a41, a51, a61)

@timeit
def calculate_1b(p, u1, u2, u3, u1_, u2_, u3_):

	a1 = np.array([
		[(u1+1)%p, (2*u2-u3)%p, (2*u3-u2)%p], 
       	[u2%p,     (u1+u3+1)%p, (u2-u3)%p  ],
       	[u3%p,     u2%p,        (u1+1-u3)%p]
	]) % p

	a2_inv = LA.inv(np.array([
		[u1_%p, (2*u2_-u3_)%p, (2*u3_-u2_)%p],
		[u2_%p, (u1_+u3_)%p,   (u2_-u3_)%p  ],
		[u3_%p, u2_%p,         (u1_-u3_)%p  ]	        
	])) % p #генерируем a2 и сразу инвертируем + берём по модулю p

	a3 = np.dot(a1, a2_inv) #перемножаем матрицы

	#берём первый столбец
	a11, a21, a31 = a3[0][0]%p, a3[1][0]%p, a3[2][0]%p

	return "Кортеж: (%i, %i)" % (a21/a11, a31/a11)
