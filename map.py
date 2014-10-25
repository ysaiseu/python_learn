#!/usr/bin/env python

def f(x):
	return x*x


print map(f,[1,2,3,4,5])

L = []
for n in [1,2,3,4,5,6]:
	L.append(f(n))
print L
