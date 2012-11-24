# -*- coding: utf-8 -*-
import time


table = {
	0: {'a5_': 0, 'a5__': 0},
	1: {'a5_': 1, 'a5__': 0},
	2: {'a5_': 2, 'a5__': 0},
	3: {'a5_': 0, 'a5__': 1},
	4: {'a5_': 1, 'a5__': 1},
	5: {'a5_': 2, 'a5__': 1},
	6: {'a5_': 0, 'a5__': 2},
	7: {'a5_': 1, 'a5__': 2},
	8: {'a5_': 2, 'a5__': 2}
}

e1 = 560941631
e2 = 384600144
e3 = 815930921
e4 = 504828919
e5 = -76835150
e6 = 112

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print 'Время вычисления: %f секунды' % (te-ts,)
        return result

    return timed

def calc_a5(a5):
	index = (a5*7) % 9
	return (table[index]['a5_'], table[index]['a5__']) 

@timeit
def calc_A1(a1, a2, a3, a4, a5):
	a5_, a5__ = calc_a5(a5)

	A1  = a1
	A2  = a2 * 4681
	A3  = a2 * 1057
	A4  = a2 * 217
	A5  = a3 * 341
	A6  = a3 * 93
	A7  = a3 * 33
	A8  = a4
	A9  = a5_
	A10 = a5__
	A11 = a5 * 9

	return (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11)

def find_A_asterisk(A5, A9):
	A5 = A5 % 3
	A9 = A9 % 3

	for index in table:
		if {'a5_': A5, 'a5__': A9} == table[index]:
			return index

@timeit
def calc_A2(A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, p):
	A_asterisk = find_A_asterisk(A5, A9)

	A1_ = A10
	A2_ = A2
	A3_ = A3
	A4_ = (e6*A1 + A4*e5 + A6*e4 + e3*A7 + A11*e2 + A_asterisk*e1) % p

	return (A1_, A2_, A3_, A4_)
