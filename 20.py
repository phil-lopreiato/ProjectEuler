#find sum of digits in 100!

fact = 1
for x in range (1,100):
	fact = fact * x

sum =00 
while fact:
	sum = sum + fact%10
	fact = fact / 10

print sum
