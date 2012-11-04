from numpy import linalg as LA
import numpy as np


p  = 1461501637330902918203684832716283019655932542983

v1 = 7584765478654
v2 = 989438574431

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
        
])) 

a3 = np.dot(a1, a2_inv)

print a3