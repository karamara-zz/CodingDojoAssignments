
import datetime
start = datetime.datetime.now()
import random
a = []
for x in range(0,10000):
	num = random.randint(0,10000)
	a.append(num)
for i in range(0,len(a)-1):
	temp=i
	for b in range (i,len(a)):
		if a[i]>a[b] and a[temp]>a[b]:
			temp=b
	(a[i],a[temp]) = (a[temp],a[i])

print a
end = datetime.datetime.now()
print "Time it took to generate and sort the list is " + str(end - start)+" microsecond(s)."