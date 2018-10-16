x=[]
print(" enter 5 elements in set A\n")
for i in range(0,5):
	x.append(int(input()))
	
setA = set(x)
	
print(" enter 5 elements in set B\n")
for i in range(0,5):
	x.append(int(input()))
	
setB = set(x)

print(" union of sets \n")
print(setA | setB)

print(" intersection of sets \n")
print(setA & setB)

print( " difference of sets \n")
print(setA - setB)

print("symmetric difference \n")
print(setB.symmetric_difference(setA))

if setA < setB:
	print("set A is subset of setB")

if setB < setA:
	print("set B is subset of setA")
	
