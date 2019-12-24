import numpy as l
a=input("enter 1st array::");
b=input("enter 2nd array::");
#using numpy
c=l.append(a,b);
print ("appended array using numpy::",c);
#using for loop
for i in range(0,len(b)):
	a.append(b[i])
print ("appended array using for loop::",a);
 
