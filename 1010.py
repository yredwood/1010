import random

Target = []

Lower = 0
Upper = 100
Count = 15

for i in xrange(Count):
	Target.append(random.randint(Lower, Upper));

print Target

def bublebuble(target):
	length = len(Target)
	for i in range(length-1):
		for j in range(i, length-1):
			if target[j] > target[j+1]:
				temp = target[j]
				target[j] = target[j+1]
				target[j+1] = temp

	return target


print bublebuble(Target)
