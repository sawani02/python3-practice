#modify the letter in sublist using indexing

lst1= ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 's'
lst2[2][1] = 'd'

print lst2