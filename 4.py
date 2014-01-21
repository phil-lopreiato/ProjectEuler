largest = 0

def isPalindrome(num):
	return str(num) == str(num)[::-1]

for x in range (100,999):
	for y in range (100,999):
		prod = x*y
		if(isPalindrome(prod) and prod > largest):
			largest = prod


print largest
		
