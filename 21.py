max=10000
sumAms = 0

def d(n):
	s = 0
	for i in range (1,n):
		if(n%i==0):
			s+=i
	return s

for i in range(1,max):
	sumi = d(i)
	if(sumi > i and sumi < max):
		sumj = d(sumi)
		if(sumj == i):
			sumAms += (i + sumi)		

print sumAms
