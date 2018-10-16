


import binascii
from termcolor import colored
from colorama import Fore
import random
import time
import cv2
from PIL import Image

kg=4
'''
def fun():
	print()
	print("************DIFFIE HELMANN KEY EXCHANGE*************")
	print()
	print("There are 2 stations communicating B and C...")
	n = input('Choose n: ')
	a = input('Choose a: ')

	print("Now n and a is sent publicly on network by B")

	t = time.time()
	kb=int(str(t-int(t))[2:])%10
	mb=(a**kb)%n
	print("Value sent by B is:",mb)

	t = time.time()
	kc=int(str(t-int(t))[2:])%10
	print(kc)
	mc=(a**kc)%n
	print("Value sent by C is:",mc)

	k1=(mc**kb)%n
	k2=(mb**kc)%n
	
	
	kg=k1
	#print kg
	print(k1,k2)
	if k1==k2:
		print('Therefore receiver should look at the following bit of r,g,b to get steganographic message',k1)

#while kg>3 or kg==0:
#	fun()

fun()
'''
k1=3
kee=""
print "Enter secret message to insert: "
kee=raw_input()
len_msg=len(kee)
u=0
lee=3
fres=""
while u<len(kee):
	print ord(kee[u])
	o=bin(ord(kee[u]))
	o=o[2:]
	if len(o)<9:
		r=9-len(o)
		while r>0:
			o="0"+o
			r-=1
	fres+=o
	#print fres
	#print("")
	u+=1
print fres

im = Image.open("/home/ubuntu/Downloads/sky1.jpeg")
rgb_im = im.convert('RGB')

im1 = Image.open("/home/ubuntu/Downloads/sky2.jpeg")
rgb_im1 = im1.convert('RGB')

width = rgb_im.size[0]
height = rgb_im.size[1]
row = 0
col = 0
pix = 0
it=0
rowdata = ""
strput1=""
strput2=""
strput3=""
a=4
r12=8
k=a
cnt=0
koi=[]
tuy=(0,0,0)
print()
print("************INSERTING MESSAGE IN IMAGE*************")
print()
	#inserting secret message in image
while row < height and it<len(fres):
	cnt=0
    	while col < width and it<len(fres):
		if cnt==k:
			r1, g1, b1 = rgb_im.getpixel((col, row))
				
			lstr=list(tuy)	
			lstr[0]=r1
			lstr[1]=g1
			lstr[2]=b1
			tuy=tuple(lstr)
			koi.append(tuy)	
			
			str1 = bin(r1)
			list1 = list(str1)
			list1[-1*k1] = fres[it]
			str1 = ''.join(list1)
			strput1=str1
			str1=str1[0:-k1]+colored(str1[-k1],"red")+str1[-k1+1:]	
			it+=1

			str2 = bin(g1)
			list2 = list(str2)
			list2[-1*k1] = fres[it]
			str2 = ''.join(list2)
			strput2=str2
			str2=str2[0:-k1]+colored(str2[-k1],"red")+str2[-k1+1:]			
			it+=1

			str3 = bin(b1)
			list3 = list(str3)
			list3[-1*k1] = fres[it]
			str3 = ''.join(list3)
			strput3=str3
			str3=str3[0:-k1]+colored(str3[-k1],"red")+str3[-k1+1:]
			it+=1
	
			r,g,b=str1,str2,str3 
			rin1=int(strput1, 2)
			gin1=int(strput2,2)
			bin1=int(strput3,2)
			rgb_im1.putpixel((col, row ),(rin1,gin1,bin1))
			k+=r12	
			col=0
				#row+=1		
				
			break
		cnt+=1
		col = col + 1
		pix = pix + 1
		
	rowdata = ""
	row = row + 2
	col = 0

rgb_im1.save("sky3.jpeg")

#showing that image got affected
print("")
print("************SHOWING IMAGE CHANGED BITS*************")
print("")
im = Image.open("/home/ubuntu/Downloads/sky3.jpeg")
rgb_im = im.convert('RGB')

width = rgb_im.size[0]
print width
height = rgb_im.size[1]
print height
row = 0
col = 0
pix = 0
it=0
rowdata = ""
flag=0 
a=4
r12=8
k=a
cnt=0
rowdata_res1=""
while row < height  and it<len(fres):
	cnt=0
	print("ROW: ",row)
	while col < width  and it<len(fres):
		if cnt==k:
			r1, g1, b1 = rgb_im.getpixel((col , row ))
			str1 = bin(r1)
			list1 = list(str1)
			if flag==0:
				list1[-1*k1] = fres[it]
			str1 = ''.join(list1)
			str_normal1=str1
			str1=str1[0:-k1]+colored(str1[-k1],"red")+str1[-k1+1:-k1+1]	
			it+=1
			if it>=len(fres):
				flag=1
			str2 = bin(g1)
						
			list2 = list(str2)
			if flag==0:		
				list2[-1*k1] = fres[it]
			str2 = ''.join(list2)
			str_normal2=str2
			str2=str2[0:-k1]+colored(str2[-k1],"red")+str2[-k1+1:-k1+1]			
			it+=1
			if it>=len(fres):
				flag=1
	
			str3 = bin(b1)
		
			list3 = list(str3)
			if flag==0:		
				list3[-1*k1] = fres[it]
			str3 = ''.join(list3)
			str_normal3=str3
			str3=str3[0:-k1]+colored(str3[-k1],"red")+str3[-k1+1:-k1+1]
			it+=1
			if it>=len(fres):
				flag=1
	
			r,g,b=str1,str2,str3 
			#if it>=len(fres):
			#	rowdata += "(" + str(str_normal1) + "," + str(str_normal2) + "," + str(str_normal3) + ") "
			#else:
			rowdata += "(" + str(r) + "," + str(g) + "," + str(b) + ") "
			rowdata_res1+="(" + str(r) + "," + str(g) + "," + str(b) + ") "
			k+=r12
			cnt+=1
			
			col=0
			print(rowdata)	
			rowdata=""
			break
		else:
			r1, g1, b1 = rgb_im.getpixel((col , row ))
			str1 = bin(r1)
			list1 = list(str1)
			str1 = ''.join(list1)
			str_normal1=str1
			str1=str1[0:-k1]+colored(str1[-k1],"red")+str1[-k1+1:]	
			
			
			str2 = bin(g1)
			list2 = list(str2)
			str2 = ''.join(list2)
			str_normal2=str2
			str2=str2[0:-k1]+colored(str2[-k1],"red")+str2[-k1+1:]			
			
			str3 = bin(b1)
			list3 = list(str3)
			str3 = ''.join(list3)
			str_normal3=str3
			str3=str3[0:-k1]+colored(str3[-k1],"red")+str3[-k1+1:]

			r,g,b=str1,str2,str3 	
			rowdata += "(" + str(str_normal1) + "," + str(str_normal2) + "," + str(str_normal3) + ") "
			cnt+=1
		
		col = col + 1
		pix = pix + 1
	#print(rowdata)	
	rowdata = ""
	row = row + 2
	col = 0


#RSA algo
print()
print("************ENCRYPTION USING RSA ALGORITHM*************")
print()
p=int(input('Enter prime p greater than 20 as RSA is made for higher primes: ')) #for proof run rsa.py program for smaller primes
q=int(input('Enter prime q greater than 20 and less than p: '))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
print("Choose an e from a below coprimes array:\n")
print(str(coprimes(phi)) + "\n")
e=int(input())
d=modinv(e,phi)
print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")


im1 = Image.open("/home/ubuntu/Downloads/sky3.jpeg")
rgb_im1 = im1.convert('RGB')

width = rgb_im1.size[0]
height = rgb_im1.size[1]
row = 0
col = 0
pix = 0
it=0
rowdata = ""
flag=0 
a=4
r12=8
k=a
cnt=0
lo=[]
list_orig_enc=[]
rowdata=[]
tuy1=(0,0,0)
koi1=[]
while row < height and it<len(fres):
	cnt=0
	rowdata=[]
	while col < width and it<len(fres):
		rowdata=[]
		if cnt==k:
			r1, g1, b1 = rgb_im1.getpixel((col , row))
					
					
			lstr=list(tuy1)	
			lstr[0]=r1
			lstr[1]=g1
			lstr[2]=b1
			tuy1=tuple(lstr)
			koi1.append(tuy1)	

			s=r1
			ri=(s**e)%n
			ri1=ri
			lo.append(r1)
			while ri>64:
				ri=ri-10

			#print(ri)	
		
			s=g1
			gi=(s**e)%n
			gi1=gi
		
			while gi>64:
				gi=gi-10

			#print(gi)	

			s=b1
			bi=(s**e)%n
			bi1=bi
		
			while bi>64:
				bi=bi-10

			#print(bi)	
			rgb_im1.putpixel((col , row),(ri1,gi1,bi1))
			it+=3
			k+=r12				

			rowdata.append(ri1)
			rowdata.append(gi1)
			rowdata.append(bi1)			
			#lst = list(rowdata)
			#lst[0] = ri1
			#lst[1]=gi1
			#lst[2]=bi1
			#rowdata	 = tuple(lst)
			list_orig_enc.append(rowdata)
			
			cnt+=1
			
			break
		col=col+1
		cnt+=1
	row = row + 2
	col = 0
print("out")
print(koi1)
print(list_orig_enc)
print(koi)
rgb_im1.save("sky9.jpeg")

print()
print("************DECRYPTING AND STORING AS ORIGINAL IMAGE*************")
print()
#Decoding and saving as normal image
im1 = Image.open("/home/ubuntu/Downloads/sky9.jpeg")
rgb_im1 = im1.convert('RGB')


width = rgb_im.size[0]
height = rgb_im.size[1]
row = 0
col = 0
pix = 0
it=0
rowdata = ""
flag=0 
a=4
r12=8
k=a
cnt=0
u=0
j=0
while row < height and it<len(fres):
	cnt=0
	print row
	while col < width and it<len(fres):
			
		if cnt==k:
			#r1, g1, b1 = rgb_im1.getpixel((col-1, row - 1))
			#r1, g1, b1 = rgb_im1.getpixel((col, row - 1))
			#r1, g1, b1 = rgb_im1.getpixel((col, row )) 
						
			r1=list_orig_enc[u][0]	
			g1=list_orig_enc[u][1]	
			b1=list_orig_enc[u][2]	
			
			u+=1
			
			#while r1<>list_orig_enc[u][0]:
			#	r1=r1+10
		
			ri1=(r1**d)%n
	
			print("")
					
			print(ri1)
			print(r1)			
			print lo[j]
			print("")
			j+=1
			#print(ri1)
		
			#while g1<>list_orig_enc[u][1]:
			#	g1=g1+10

			gi1=(g1**d)%n
			#print(gi1)

			#while b1<>list_orig_enc[u][2]:
			#	b1=b1+10

			bi1=(b1**d)%n
			#print(bi1)
			rgb_im1.putpixel((col, row ),(ri1,gi1,bi1))
			it+=3
		
			k+=r12
			break
		col=col+1
		cnt+=1
		
	row = row + 2
	col = 0
print("out2")
rgb_im1.save("sky12.jpeg")



im = Image.open("/home/ubuntu/Downloads/sky12.jpeg")
rgb_im = im.convert('RGB')

width = rgb_im.size[0]
print width
height = rgb_im.size[1]
print height
row = 0
col = 0
pix = 0
it=0
rowdata = ""
flag=0 
a=4
r12=8
k=a
cnt=0
rowdata_res2=""
fress=""
while row < height  and it<len(fres):
	cnt=0
	print(row)
	while col < width  and it<len(fres):
		if cnt==k:
			r1, g1, b1 = rgb_im.getpixel((col , row ))
			str1 = bin(r1)
			list1 = list(str1)
			if flag==0:
				list1[-1*k1] = fres[it]
			str1 = ''.join(list1)
			str_normal1=str1
			fress+=str1[-k1]
			str1=str1[0:-k1]+colored(str1[-k1],"red")+str1[-k1+1:-k1+1]	
			
			it+=1
			if it>=len(fres):
				flag=1
			str2 = bin(g1)
						
			list2 = list(str2)
			if flag==0:		
				list2[-1*k1] = fres[it]
			str2 = ''.join(list2)
			str_normal2=str2
			fress+=str2[-k1]
			str2=str2[0:-k1]+colored(str2[-k1],"red")+str2[-k1+1:-k1+1]
						
			it+=1
			if it>=len(fres):
				flag=1
	
			str3 = bin(b1)
		
			list3 = list(str3)
			if flag==0:		
				list3[-1*k1] = fres[it]
			str3 = ''.join(list3)
			str_normal3=str3
			fress+=str3[-k1]
			str3=str3[0:-k1]+colored(str3[-k1],"red")+str3[-k1+1:-k1+1]
			it+=1
			if it>=len(fres):
				flag=1
	
			r,g,b=str1,str2,str3 
			#if it>=len(fres):
			#	rowdata += "(" + str(str_normal1) + "," + str(str_normal2) + "," + str(str_normal3) + ") "
			#else:
			rowdata += "(" + str(r) + "," + str(g) + "," + str(b) + ") "
			rowdata_res2 += "(" + str(r) + "," + str(g) + "," + str(b) + ") "
			r23=str(r)
			g23=str(g)
			b23=str(b)				
				#print r23[-1]
				#final_string+=r23[-1]+g23[-1]+b23[-1]
			k+=r12
			cnt+=1
			
			col=0
			print(rowdata)
			print rowdata[-1]	
			rowdata=""
			break
		else:
			r1, g1, b1 = rgb_im.getpixel((col , row ))
			str1 = bin(r1)
			list1 = list(str1)
			str1 = ''.join(list1)
			str_normal1=str1
			str1=str1[0:-k1]+colored(str1[-k1],"red")+str1[-k1+1:]	
			
			
			str2 = bin(g1)
			list2 = list(str2)
			str2 = ''.join(list2)
			str_normal2=str2
			str2=str2[0:-k1]+colored(str2[-k1],"red")+str2[-k1+1:]			
			
			str3 = bin(b1)
			list3 = list(str3)
			str3 = ''.join(list3)
			str_normal3=str3
			str3=str3[0:-k1]+colored(str3[-k1],"red")+str3[-k1+1:]

			r,g,b=str1,str2,str3 	
			rowdata += "(" + str(str_normal1) + "," + str(str_normal2) + "," + str(str_normal3) + ") "
			cnt+=1
		
		col = col + 1
		pix = pix + 1
	#print(rowdata)	
	rowdata = ""
	row = row + 2
	col = 0

print("")
print("BITS OF ORIGINAL IMAGE:")
print(rowdata_res1)
print("")
print("BITS AFTER DECRYPTING FROM RSA ALGORITHM:")
print(rowdata_res2)
print("The secret message was:")

print(fress)
fress_len=len(fress)
p=0
secret=""
while p<fress_len:
	string=fress[p:p+9]
	aux_str=str(string)
	print aux_str
	letter = int(aux_str, 2)
	
				
				
	fletter=binascii.unhexlify('%x' % letter)
				
	secret+=fletter
	p+=9	
print(secret)


print("-----------------REMOVING SALT AND PEPPER NOISE USING FILTERING TECHNIQUE------------------")
 
image1="sky9.jpeg"

image = cv2.imread(image1)

processed_image = cv2.medianBlur(image, 3)



cv2.imwrite('processed_image.png', processed_image)

cv2.waitKey(0)

