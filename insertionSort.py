
import datetime
start = datetime.datetime.now()
import random
a = []
for x in range(0,10000):
	num = random.randint(0,10000)
	a.append(num)
for i in range (0,len(a)):
	for b in range (i,0,-1):
		if a[b]<a[b-1]:
			(a[b],a[b-1])=(a[b-1],a[b])
		else:
			break
print a
