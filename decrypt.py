#coded.txt is the coded message file
#n.txt is the file containing the public key
#Enter private key through command line interface
import os
import sys
from datetime import datetime
def time_now():
	now=(datetime.now()).strftime('%c')
	now="["+now+"]:"
	return now

def loading(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sys.stdout.write('\r')
    sys.stdout.flush()

def decode(c):
    m=pow(c,d)%n
    return(m)



time1=time_now()
try:
    outfile1=open("coded.txt","r")
    outfile3=open("n.txt","r")
except:
    print('Please run encrypt.py to generate the required coded text file and public key file')
    input()
    exit()
n=int(outfile3.read())
decoded=[]
coded=[]
coded1=[]
#Arrived at a list of decoded message
#Convert numbers to char
try:
    d=int(raw_input("Enter the key:"))
except:
    d=int(input("Enter the key:"))
coded1=(outfile1.read()).split(",")
length=len(coded1)
for i in range(len(coded1)):
    coded.append(int(coded1[i]))

count=0
for i in coded:
    count+=1
    prompt="Decoding "+str(int(count*100/length))+"%"
    loading(prompt)
    decoded.append(decode(i))
count=0

for i in range(len(decoded)):
    decoded[i]=chr(decoded[i])
output=""
for i in range(len(decoded)):

    output=output+decoded[i]
print("Writing message to file")
print()
outfile1.close()
outfile3.close()

output_list=[x for x in output.split(";")]
outfile=open("passwords_out.txt","w")
for x in output_list:
    str=x+"\n"
    outfile.write(str)
outfile.close()
time2=time_now()
print("Started at:",time1[:-1])
print("Ended at  :",time2[:-1])
try:
    raw_input()
except:
    input()
