# -*- coding: utf-8 -*-
from util import *


p  = 1461501637330902918203684832716283019655932542983 #некое большое число

#задаём начальные значения
v1 = 1461501637330902918203684832716283019655932542981
v2 = 1461501637330902918203684832716283019655932542982

#для второго задания
u1,  u2,  u3  = 1546545, 267654654, 36544764754
u1_, u2_, u3_ = 1654654, 134265465, 43313893654


if __name__ == '__main__':	
	calculate_1a(p, v1, v2)
	calculate_1b(p, u1, u2, u3, u1_, u2_, u3_)
