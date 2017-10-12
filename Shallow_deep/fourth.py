# deep copy

""" Deep copy makes a copy of the list and then do changes on it"""


from copy import deepcopy

lst1 = ['a', 'b', 'c', 'd']
lst2 = deepcopy(lst1)

lst2[3] = 's'

print lst2
print lst1
