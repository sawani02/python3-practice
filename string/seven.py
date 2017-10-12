""" write a program to reverse the 
given input
Logic: get the list
get the length of the list 
the length will help the index to get to the end element of the list
while loop
"""

def reverse(list):

	j=len(list)-1
	while(j>=0):
		print("string: %s" % list[j])
		j-=1

list=["abc","def", "sav"]
reverse(list)

