# -*- coding: utf-8 -*-
from util import *


p  = 1461501637330902918203684832716283019655932542983 #некое очень большое число

#для первого задания
v1_default = p - 168595435
v2_default = p - 25437587438

#для второго задания
u1_default,  u2_default,  u3_default  = 432678, 1, 1
u1__default, u2__default, u3__default = 234324, 11, 146


if __name__ == '__main__':
	#задаём начальные значения для первого задания
	try:
		v1 = int(input('Введите число v1(по умолчанию будет взято число %i): ' % v1_default))
	except:
		v1 = v1_default
	else:
		if v1 > p:
			v1 = v1_default 

	try:
		v2 = int(input('Введите число v2(по умолчанию будет взято число %i): ' % v2_default))
	except:
		v2 = v2_default
	else:
		if v2 > p:
			v2 = v2_default 

	calculate_1a(p, v1, v2)

	#задаём начальные значения для второго задания
	try:
		u1 = int(input('Введите число u1(по умолчанию будет взято число %i): ' % u1_default))
	except:
		u1 = u1_default
	else:
		if u1 > p:
			u1 = u1_default 

	try:
		u2 = int(input('Введите число u2(по умолчанию будет взято число %i): ' % u2_default))
	except:
		u2 = u2_default
	else:
		if u2 > p:
			u2 = u2_default

	try:
		u3 = int(input('Введите число u3(по умолчанию будет взято число %i): ' % u3_default))
	except:
		u3 = u3_default
	else:
		if u3 > p:
			u3 = u3_default 

	try:
		u1_ = int(input('Введите число u1-штрих(по умолчанию будет взято число %i): ' % u1__default))
	except:
		u1_ = u1__default
	else:
		if u1_ > p:
			u1_ = u1__default 

	try:
		u2_ = int(input('Введите число u2-штрих(по умолчанию будет взято число %i): ' % u2__default))
	except:
		u2_ = u2__default
	else:
		if u2_ > p:
			u2_ = u2__default 

	try:
		u3_ = int(input('Введите число u3-штрих(по умолчанию будет взято число %i): ' % u3__default))
	except:
		u3_ = u3__default
	else:
		if u3_ > p:
			u3_ = u3__default 

	calculate_1b(p, u1, u2, u3, u1_, u2_, u3_)
