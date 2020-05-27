#Store text in a file passwords.txt
import os
import sys
import random
coded=[]
decoded=[]
from datetime import datetime
def time_now():
	now=(datetime.now()).strftime('%c')
	now="["+now+"]:"
	return now


def file_to_string():
	string=""
	try:
		infile=open("passwords.txt","r")
		string = infile.read()
		return(string)
		infile.close()
	except:
		print("Please store the passwords in a text file passwords.txt")
		input()
def loading(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sys.stdout.write('\r')
    sys.stdout.flush()

def find_primes():
    start = 200
    end = 400
    list=[]
    for val in range(start, end + 1):

        # If num is divisible by any number
        # between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
                else:
                    if(val-1==n):
                        list.append(val)

    random_no1=random.randint(1,len(list))
    p=list[random_no1]
    while 1:
        random_no=random.randint(1,len(list))
        if random_no!=random_no1:
            break
    q=list[random_no]
    return(p,q)


def encode(m):
    global e,n
    c=pow(m,e)%n
    return(c)

def main():
	time1=time_now()
	global e,n

	p,q=find_primes()
	n=p*q
	phi=(p-1)*(q-1)
	e=65537
	i=0
	while(1):
	    if((phi*i+1)%e==0):
	        d=(phi*i+1)/e
	        break
	    i+=1
	d=int(d)
	coded_str=""
	string=file_to_string()
	length=len(string)
	count=0
	for i in string:
	    count+=1
	    prompt="Encoding in progress: "+str(int(count*100/length))+"%"
	    loading(prompt)
	    coded.append(encode(ord(i)))
	count=0
	coded_str=""
	coded_str1=""
	for i in coded:
	    coded_str1=coded_str1+str(i)+","
	print("Make a note of the key for decryption:",d)
	coded_str=coded_str1[:-1]
	outfile1=open("coded.txt","w")
	outfile3=open("n.txt","w")
	outfile1.write(coded_str)
	outfile3.write(str(n))
	outfile1.close()
	outfile3.close()
	time2=time_now()
	print("Started at:",time1[:-1])
	print("Ended at  :",time2[:-1])
	input()


main()
