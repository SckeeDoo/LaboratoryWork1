import time
import matplotlib.pyplot as plt
from matplotlib import pyplot as PLT
from numpy import *

A = []
B = []
C = []

def Fib1(n):
	if n<2:
		return n
	return Fib1(n-1) + Fib1(n-2)

def Fib2(n):
	i = 1
	j = 0
	for k in range(1,n+1):
		j = i + j
		i = j - i
	return j

def Fib3(n):
	i = 1
	j = 0
	k = 0
	h = 1
	while n>0:
		if (n % 2 == 1): 
			t = j*k
			j = i * h + j * k + t
			i = i * k + t
		t = h ** 2
		h = 2 * k * h + t
		k = k ** 2 + t
		n = n / 2
	return j

def Time(function,argument):
	start = time.time()
	function(argument)
	end = time.time()
	return end - start

n = 10000

for i in range(n):
	#A.append(Time(Fib1,i))
	B.append(Time(Fib2,i))
	C.append(Time(Fib3,i))


plt.plot(B)
plt.show()
plt.plot(C)
plt.show()




