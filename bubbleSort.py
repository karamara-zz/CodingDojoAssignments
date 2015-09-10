import datetime
start = datetime.datetime.now()
import random
list = []

for x in range(0,100):
	num = random.randint(0,10000)
	list.append(num)
for k in range (0,len(list)):
	for b in range (0,len(list)-1):
		if list[b] > list[b+1]:
			(list[b+1],list[b])=(list[b],list[b+1])
print list
end = datetime.datetime.now()
print "Time it took to generate and sort the list is " + str(end - start)+" microsecond(s)."