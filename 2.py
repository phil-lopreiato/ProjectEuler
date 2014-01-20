val1 = 1
val2 = 2
sum = 0

while (val2 <= 4000000):
	if(val2%2 ==0):
		sum += val2
	temp = val2
	val2 += val1
	val1 = temp

print sum
