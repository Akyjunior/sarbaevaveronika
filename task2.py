# -*- coding: utf-8 -*-
from util2 import calc_A1


p  = 2**30 - 1 #некое очень большое число

#для первого задания
a1 = p - 1
a2 = p - 2
a3 = p - 3
a4 = p - 4
a5 = p - 5

if __name__ == '__main__':
	
	#первая часть задачи
	calc_A1(a1, a2, a3, a4, a5)

	#вторая часть задачи
	#print 'Кортеж A2: ' % calc_A2(A10, A2, A3, A5, A9)
