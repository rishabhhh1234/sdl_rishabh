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

    

