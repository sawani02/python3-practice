# omit first and last element of #string

str="sawani"

print str[1:-1]


def rotate(str,n):
 	return str[n:] + str[:n]

print (rotate(str,2))

print str[2:] + str [:2]
