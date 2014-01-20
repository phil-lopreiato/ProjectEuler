from math import sqrt

def isPrime(num):
        i=3
        while(i<sqrt(num)):
                if(num%i==0):
                        return False
                i+=2
        return True


largest = 0
num = 600851475143
i=3

while(i<sqrt(num)):
	if(num%i==0 and isPrime(i)):
		print i
		largest = i
	i+=2
print largest
		
