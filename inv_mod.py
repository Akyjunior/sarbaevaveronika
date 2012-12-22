# -*- coding: utf-8 -*-
n = n_orig = 97
m = m_orig = 30

A=[1,0]
B=[0,1]

def r(n,m):
	return n % m

def q(n, m):
	return n // m

def a(i, q, A):
	return A[i-1] - q*A[i]

def b(i, q, B):
	return B[i-1] - q*B[i]

i = 1
while n > 1:
	_r = r(n, m)
	_q = q(n, m)
	_a = a(i, _q, A) 
	_b = b(i, _q, B)
	A.append(_a)
	B.append(_b)

	print "n=%s, m=%s, Ri=%s, Qi=%s, ai=%s, bi=%s" % (n, m, _r, _q, _a, _b)
	n = m
	m = _r
	i = i + 1

result = B[i - 1]

if result < 0:
	result = result + n_orig

print "Ответ: 1/detA = %s " % result

#проверяем результат
print "Проверяем результат: (%s*%s)mod(%s) => %s " % (m_orig, result, n_orig, (m_orig*result) % n_orig)