import random

Target = []

Lower = 0
Upper = 100
Count = 15

for i in xrange(Count):
	Target.append(random.randint(Lower, Upper));


# def bubblesort(a) :
# 	count = 1
# 	for i in range(0,len(a)):
# 		for j in range(i+1, len(a)):

# 			if(count % 10 == 1 and count % 100 != 11) :
# 				print "....",count,"st comparison...."
# 			elif(count % 10 == 2 and count % 100 != 12) :
# 				print "....",count,"nd comparison...."
# 			else:
# 				print "....",count,"th comparison...."

# 			print a[i],"(",i,") and ",a[j],"(",j,") comparison"

# 			if(a[i] > a[j]) :
# 				temp = a[i]
# 				a[i] = a[j]
# 				a[j] = temp
# 			count = count +1

# 	return a

# print bubblesort(Target)
cnt = 1
depth = 0

def quickquick(a) :
	global cnt
	global depth
	length = len(a)
	if(len(a)<=1) :
		depth = depth -1
		return a
	#print cnt,":", a, "%-s" % (depth)
	print "%2d : %-60s Depth: %d" %(cnt, a, depth)
	cnt = cnt + 1
	pivot = a[0]
	less =[]
	greater = []
	pivot_list = []
	

	for i in range(length) :
		if a[i] > pivot :
			greater.append(a[i])
		elif a[i] == pivot :
			pivot_list.append(a[i])
		else :
			less.append(a[i])

	depth = depth + 1
	less = quickquick(less)
	depth = depth + 1
	greater = quickquick(greater)
	depth = depth - 1;
	return less + pivot_list + greater

print "Output : %s" %quickquick(Target)