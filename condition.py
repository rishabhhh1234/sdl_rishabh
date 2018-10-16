### if-else loop
'''
x=float(input("Enter salary "))
if x>50000:
    print("Salary of head manager")
elif 50000< x< 100000:
    print("salary of manager")
else:
    print("salary of workers")
'''


### for loop
'''
animals=['cat','dog','goat','horse']
for a in animals:   # a will act as index
    if len(a)>4:
        print(a,len(a)) # a -> for index   len(a) -> finding length of that index
    print(a)
'''

'''
for i in range (10):
    if i%2==0:
        print ('even',i)
    else:
        print ('odd ',i)

'''
### to count the words in a string

import operator
def word_count(str):
    count=dict()
    w=string.split()
    for a in w:
        if a in count:
            count[a]+=1
        else:
            count[a]=1
    return count
string=input("enter the string")
c=word_count(string)
sorted_x = sorted(c.items(), key=operator.itemgetter(0))
print(sorted_x)
