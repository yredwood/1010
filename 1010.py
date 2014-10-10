import random

Target = []

Lower = 0
Upper = 100
Count = 100

for i in xrange(Count):
	Target.append(random.randint(Lower, Upper));

print Target

def bubblesort(a) :
	count = 1
	for i in range(0,len(a)):
		for j in range(i+1, len(a)):

			if(count % 10 == 1 and count % 100 != 11) :
				print "....",count,"st comparison...."
			elif(count % 10 == 2 and count % 100 != 12) :
				print "....",count,"nd comparison...."
			else:
				print "....",count,"th comparison...."

			print a[i],"(",i,") and ",a[j],"(",j,") comparison"

			if(a[i] > a[j]) :
				temp = a[i]
				a[i] = a[j]
				a[j] = temp
			count = count +1

	return a

print bubblesort(Target)
