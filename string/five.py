# count the number of occurances in a given string

# index gives the index in the array and i gives the value in the array

a = "aaabbccdef"

x = [0]*200

for i in a:
  x[ord(i)]=x[ord(i)]+1


for index, i in enumerate(x):
	if (i>0):
		print('%c occured %d' %(chr(index),i))
