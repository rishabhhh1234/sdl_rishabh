def cnt(str):
    w = str.split();
    count=dict();
    for a in w:
        if a in count:
            count[a]+=1;
        else:
            count[a]=1;
    return count;
str1=input("Enter string");
c=cnt(str1);
d=sorted(c.items())
print(d);
        
