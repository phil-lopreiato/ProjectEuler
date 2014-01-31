def d(n):
	d = []
	for i in range (1,n):
		if(n%i==0):
        		d.append(i)
	return sum(d)

print("n: "+str(d(input("input n: "))))
