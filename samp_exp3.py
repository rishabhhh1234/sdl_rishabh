

from Tkinter import *
#from tkFileDialog import *
from PIL import ImageTk, Image
import os
import cv2

import binascii
from termcolor import colored
from colorama import Fore
import random
import time
import PIL.Image, PIL.ImageTk
from PIL import Image

#global fres
root = Tk()

canvas=Canvas(root)
root.geometry("1400x850")
root.resizable(width=True, height=True)
root.configure(bg="#4B5320")



def fun():
	root5=Tk()
	frame=Frame(root5)
	root5.geometry("1400x850")
	root5.configure(bg="#4B5320")
	text="THANK YOU"

	text = (' '*10) + text + (' '*10)

	marquee = Text(root5, height=1, width=10,font="Times 32 bold italic",bg="#4B5320",fg="white")
	marquee.grid(row=0,column=0,padx=350,pady=270)

	i = 0	

	def command(x, i):
    		marquee.insert("0.1", x)
    		if i == len(text):
        		i = 0
    		else:
        		i = i+1
    		root5.after(100, lambda:command(text[i:i+10], i))

	button = Button(root5, text="Start", command=lambda: command(text[i:i+10], i))
	button.grid()
	fundif()

	#l6=Label(root5,text="THANK YOU.",font="Times 32 bold italic").grid(row=0,column=0,padx=450,pady=300)

	root5.mainloop()
	


	#root4=Tk()
	#frame=Frame(root4)
"""def browsefunc():
        filename =askopenfilename(title='open')
        return filename"""

d=0   
n=0 
def com():
	def fff(event):
		global fres
		global list_orig_enc
		global d
		global n
		print()
		print("************ENCRYPTION USING RSA ALGORITHM*************")
		print()
		p=int(e2.get())
		q=int(e3.get())
		e=int(e4.get())
		print(e)
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
		
		d=modinv(e,phi)
		print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
		print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")


		im1 = Image.open("/home/dell/Desktop/sky3.jpeg")
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
		#print(koi)
		rgb_im1.save("sky9.jpeg")
		root=Tk()
		root.geometry('1400x850')
		canvas=Canvas(root,width=600,height=600)
		canvas.pack()
		img=ImageTk.PhotoImage(Image.open("sky9.jpeg"),master=root)
		canvas.create_image(20,20,anchor=NW,image=img)
		root.mainloop()
	
	def ftd():
		global fres
		global list_orig_enc
		global d
		global n
		print("")
		print("************DECRYPTING AND STORING AS ORIGINAL IMAGE*************")
		print("")
		#Decoding and saving as normal image
		#rgb_im = im.convert('RGB')
		im1 = Image.open("/home/dell/Desktop/sky9.jpeg")
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
			
					#print("")
							
					#print(ri1)
					#print(r1)			
					
					#print("")
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
		root=Tk()
		root.geometry('1400x850')
		canvas=Canvas(root,width=600,height=600)
		canvas.pack()
		img=ImageTk.PhotoImage(Image.open("sky12.jpeg"),master=root)
		canvas.create_image(20,20,anchor=NW,image=img)
		root.mainloop()
		



	def sh():
		global fres
		global rowdata_res1
		im = Image.open("/home/dell/Desktop/sky12.jpeg")
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
					sstr_normal2=str2
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

		l16=Label(root10,text="The Secret Message is",font="Times 24 bold italic")
		l16.grid(row=6,column=0,padx=200,pady=50)

		l16=Label(root10,text=secret,font="Times 24 bold italic")
		l16.grid(row=6,column=1,padx=200,pady=50)

	def salt():
		print("-----------------REMOVING SALT AND PEPPER NOISE USING FILTERING TECHNIQUE------------------")
		 
		image1="sky9.jpeg"

		image = cv2.imread(image1)

		processed_image = cv2.medianBlur(image, 3)

		cv2.imwrite('masked.jpeg', processed_image)
		# Create a window
		print("---SUCCESSFULLY REMOVED---")

		root=Tk()
		root.geometry('1400x850')
		canvas=Canvas(root,width=600,height=600)
		canvas.pack()
		img=ImageTk.PhotoImage(Image.open("masked.jpeg"),master=root)
		canvas.create_image(20,20,anchor=NW,image=img)
		root.mainloop()
		

		











	root10=Tk()
	frame = Frame(root10)
	root10.configure(bg="#4B5320")
	root10.geometry('1400x850')
	l3=Label(root10,text="Encryption:",bg="yellow",fg="purple",font="Times 24 bold underline italic").grid(row=0,column=0)
	l4=Label(root10,text="Enter prime p:",bg="white",fg="purple",font="Times 15").grid(row=1,column=0,padx=200,pady=50)
	l5=Label(root10,text="Enter prime q:",bg="white",fg="purple",font="Times 15").grid(row=2,column=0,padx=200,pady=50)
	l6=Label(root10,text="choose e:",bg="white",fg="purple",font="Times 15").grid(row=3,column=0,padx=200,pady=50)
	e2 = Entry(root10)
	e3 = Entry(root10)
	e4 = Entry(root10)
	e2.grid(row=1, column=1)
	e3.grid(row=2,column=1)
	e4.grid(row=3,column=1)
	e2.bind("<Leave>", fff)
	e3.bind("<Leave>", fff)
	e4.bind("<Leave>", fff)

	b9= Button(root10, text="Decrypt",command=ftd)
	b9.grid(row=4,column=0,padx=200)

	b10= Button(root10, text="show message",command=sh)
	b10.grid(row=4,column=1,padx=200)

	b11= Button(root10, text="Masking",command=salt)
	b11.grid(row=5,column=1,padx=200,pady=50)

	b13= Button(root10, text="next",command=fun)
	b13.grid(row=7,column=2,padx=200,pady=50)

	
	"""def returnEntry(arg=None):
	Gets the result from Entry and return it to the Label
 
	result = myEntry.get()
	resultLabel.config(text=result)
	myEntry.delete(0,END)
 
	# Create the Entry widget
	myEntry = Entry(root10, width=20)
	myEntry.focus()
	myEntry.bind("<Return>",returnEntry)
	myEntry.grid()
	 
	# Create the Enter button
	enterEntry = Button(root10, text= "Enter", command=returnEntry)
	enterEntry.grid(row=6)
	 
	# Create and emplty Label to put the result in
	resultLabel = Label(root10, text = "")
	resultLabel.grid()"""




	"""l6=Label(root10,text="Enter e value:",bg="white",fg="purple",font="Times 15").grid(row=0,column=0,padx=200,pady=50)
	pathlabel = Label(root10)
	pathlabel.grid(row=0,column=1,padx=220)
	e5 = Entry(root10)
	e5.grid(row=0,column=1)

	text="SUCCESSFULLY ENCODED"

	text = (' '*20) + text + (' '*20)

	marquee = Text(root10, height=1, width=20,font="Times 32 bold italic")
	marquee.grid(row=1,column=0,padx=200,pady=100)

	i = 0	

	def command(x, i):
    		marquee.insert("0.1", x)
    		if i == len(text):
        		i = 0
    		else:
        		i = i+1
    		root10.after(100, lambda:command(text[i:i+20], i))

	bon = Button(root10, text="Start", command=lambda: command(text[i:i+20], i))
	bon.grid()

	b5 = Button(root10, text="NEXT",command=fun)
	b5.grid(pady=100)"""


	
	root10.mainloop()
fres=""
list_orig_enc=[]
rowdata_res1=""
def new_func():
	def callback(event):
	    	global fres	
		kee=e1.get()
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
	k1=4
	def call(event):
		global k1
		print()
		print("************DIFFIE HELMANN KEY EXCHANGE*************")
		print()
		
		print("There are 2 stations communicating B and C...")
		
		print("Now n and a is sent publicly on network by B")
		
		n=int(e2.get())
		a=int(e3.get())
		t = time.time()
		kb=int(str(t-int(t))[2:])%10
		mb=(a**kb)%n
		print("Value sent by B is:",mb)

		t = time.time()
		kc=int(str(t-int(t))[2:])%10
		print(kc)
		mc=(a**kc)%n
		print("Value sent by C is:",mc)

		kg=(mc**kb)%n
		k2=(mb**kc)%n
		
		
		k1=kg
		#print kg
		print(kg,k2)
		if kg==k2:
			print('Therefore receiver should look at the following bit of r,g,b to get steganographic message',kg)
	
	def calla():
		global fres
		print("---Inserting message in image---")
		im = Image.open("/home/dell/Desktop/sky1.jpeg")
		rgb_im = im.convert('RGB')

		im1 = Image.open("/home/dell/Desktop/sky2.jpeg")
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
		print("---message is inserted---")
		root=Tk()
		root.geometry('1400x850')
		canvas=Canvas(root,width=600,height=600)
		canvas.pack()
		img=ImageTk.PhotoImage(Image.open("sky1.jpeg"),master=root)
		canvas.create_image(20,20,anchor=NW,image=img)
		root.mainloop()
		mainloop()


	def funct():
		global fres
		print("")
		print("************SHOWING IMAGE CHANGED BITS*************")
		print("")
		im = Image.open("/home/dell/Desktop/sky3.jpeg")
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
		global rowdata_res1
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
		print("Bits changed")
	



	root1=Tk()
	frame = Frame(root1)
	root1.configure(bg="#4B5320")
	"""ratio = 1
	vertical_edge_len =1000

	vertical = Frame(root1, bg='black', height=ratio * vertical_edge_len,
                                                                   width=1)
	vertical.place(x=650, y=0)"""
    

	root1.geometry('1400x850')

	#l2=Label(root1,text="select image:",bg="white",fg="purple",font="Times 15").grid(row=0,column=0)
	"""b1 = Button(root1, text="Browse", command=defi)
	b1.grid(row=0,column=1,padx=20)"""
	l1=Label(root1,text="Enter text:",bg="white",fg="purple",font="Times 15").grid(row=4,column=0,pady=50)
	l1=Label(root1,text="Use Diffie hellman:",bg="white",fg="purple",font="Times 15").grid(row=5,column=0,pady=50)
	l10=Label(root1,text="choose n:",bg="white",fg="purple",font="Times 15").grid(row=6,column=0,pady=50)
	l11=Label(root1,text="choose a:",bg="white",fg="purple",font="Times 15").grid(row=7,column=0,pady=50)
	#l3=Label(root1,text="Show image changed bits:",bg="white",fg="purple",font="Times 15").grid(row=7,column=0,padx=200,pady=50)
	#l3=Label(root1,text="Encryption:",bg="yellow",fg="purple",font="Times 24 bold underline italic").grid(row=6,column=0)
	#l4=Label(root1,text="Enter prime p:",bg="white",fg="purple",font="Times 15").grid(row=8,column=0,padx=200,pady=50)
	#l5=Label(root1,text="Enter prime q:",bg="white",fg="purple",font="Times 15").grid(row=9,column=0,padx=200,pady=50)
	#l6=Label(root1,text="Enter e value:",bg="red",fg="purple",font="Times 15").grid(row=10,column=0,padx=200,pady=50)
	#b = Button(root1, text="Encode") 
	#b.grid(row=5,column=1,padx=20)
	b2= Button(root1, text="Message insertion",command=calla)
	b2.grid(row=8,column=0,padx=200)
	#l2=Label(root1,text="Received  text:",bg="red",fg="purple",font="Times 15").grid(row=4,column=5)"""



	e1 = Entry(root1)

	#kee=raw_input()

	pathlabel = Label(root1)
	pathlabel.grid(row=0,column=1,padx=220)
	e2 = Entry(root1)
	e3 = Entry(root1)
	e4 = Entry(root1)
	#e5 = Entry(root1)
	#e6 = Entry(root1)
	e1.grid(row=4,column=1)
	e2.grid(row=6, column=1)
	e3.grid(row=7,column=1)
	#e4.grid(row=9,column=1)
	#e5.grid(row=10,column=1)
	#e6.grid(row=5,column=1)

	buto = Button(root1, text="NEXT",command=com)
	buto.grid(row=9,column=3,padx=1)
	b4 = Button(root1, text="Image changed bits",command=funct)
	b4.grid(row=9,column=2,padx=1)


	e1.bind("<Leave>", callback)
	e2.bind("<Leave>", call)
	e3.bind("<Leave>", call)
	root1.mainloop()

def ano_func():
	root2=Tk()
	frame = Frame(root2)
	
	"""ratio = 1
	vertical_edge_len =1000

	vertical = Frame(root2, bg='black', height=ratio * vertical_edge_len,
                                                                   width=1)
	vertical.place(x=650, y=0)"""
    

	root2.geometry('1400x850')
	root2.configure(bg="#15F4EE")
	l2=Label(root2,text="select audio:",bg="red",fg="purple",font="Times 15").grid(row=0,column=0,padx=200,pady=50)
	"""b1 = Button(root2, text="Browse", command=browsefunc)
	b1.grid(row=0,column=1,padx=20)"""
	l12=Label(root2,text="Encryption:",bg="yellow",fg="purple",font="Times 24 bold underline italic").grid(row=1,column=0)
	l1=Label(root2,text="Enter text:",bg="white",fg="purple",font="Times 15").grid(row=2,column=0,padx=200,pady=50)
	b = Button(root2, text="Encode") 
	b.grid(row=3,column=1,padx=20,pady=50)
	#b2= Button(root2, text="")
	#b2.grid(row=1,column=5,padx=140)
	b1 = Button(root2, text="Browse stegano audio")
	b1.grid(row=0,column=1,padx=20)
	
	#l2=Label(root2,text="Received  text:",bg="red",fg="purple",font="Times 15").grid(row=4,column=5)
	


	e1 = Entry(root2)
	pathlabel = Label(root2)
	pathlabel.grid(row=1,column=1,padx=220)

	#e2 = Entry(root2)

	e1.grid(row=2,column=1)
	#e2.grid(row=4, column=6)
	#pathlabel = Label(root2)
	#pathlabel.grid(row=0,column=1,padx=220)

	root2.mainloop()


def func():
	root3=Tk()
	frame = Frame(root3)
	root3.geometry('1400x850')
	root3.configure(bg="#4B5320")
	
	l3=Label(root3,text="select option:",bg="yellow",fg="purple",font="Times 24 bold underline italic").grid(row=8,column=0)

	b3 = Button(root3, text="1.IMAGE STEGANOGRAPHY", command=new_func)
	b3.grid(row=9,column=1,padx=20)
	b4 = Button(root3, text="2.AUDIO STEGANOGRAPHY", command=ano_func)
	b4.grid(row=10,column=1,padx=20)
	root3.mainloop()

#l5=Label(root,text="WELCOME TO THE\nWORLD OF STEGANOGRAPHY.",font="Times 32 bold italic").grid(row=0,column=0,padx=280,pady=270)

text="WELCOME TO THE WORLD OF STEGANOGRAPHY"

text = (' '*20) + text + (' '*20)

marquee = Text(root, height=1, width=20,font="Times 32 bold italic",bg="#4B5320",fg="white")
marquee.grid(row=0,column=0,padx=350,pady=270)

i = 0

def command(x, i):
    marquee.insert("0.1", x)
    if i == len(text):
        i = 0
    else:
        i = i+1
    root.after(100, lambda:command(text[i:i+20], i))

but = Button(root, text="CONTINUE",command=func)
but.grid(row=1,column=1,sticky=E,padx=1)


#button = Button(root, text="Start", command=lambda: command(text[i:i+20], i))
#button.grid()




"""canvas.grid()

canvas_text = canvas.create_text(20, 20, text='', anchor=NW)

test_string = "WELCOME TO THE\n WORLD OF STEGANOGRAPHY"
#Time delay between chars, in milliseconds
delta = 500 
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta"""

#but = Button(root, text="CONTINUE",command=func)
#but.grid(row=1,column=1,sticky=E,padx=1)

button = Button(root, text="Start", command=lambda: command(text[i:i+20], i))
button.grid()


root.mainloop()


