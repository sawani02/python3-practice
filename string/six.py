""" write a program convert all the owels to uppercase for the given input string
1. get the string 
for each character in the string{
	if the char belongs to any of the vowels
	then go to ascii value of character
	subtract 32 from ascii value
	convert ascii value back to character
	append the converted character into new string
	else
	append the character in the new string"
	} """


def vowel(str):
 index = 0
 new_str=""
 for i in str:
  #if (i=='a') or (i=='e'), or (i=='i'), or (i=='o') or (i=='u'):

  if i in 'aeiou':
  	new_str+=chr(ord(str[index])-32)

  else:
  	new_str+=str[index]

  index+=1
 return new_str

str = "abcdefghij"
print(vowel(str))
