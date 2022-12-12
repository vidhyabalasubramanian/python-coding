# We have multiple methods of List like
'''
    1.append
    2.insert
    3.extend
    4.index
    5.remove
    6.sort
    7.reverse
    8.pop'''

list=['a','b','c','d','e','f','g','h']
list1=['j','k']

list.append('i')#append method use to add the object in left of lists
print(list)
list.insert(1,'a')#insert method use to insert particular object in particular index
print(list)
list.extend(list1)#extend method use to extend the lists
print(list)
print(list.index('f'))#index method use to print particular object index
list.remove('h')#remove method use to remove listed objects
print(list)
list.sort()#sort method use to ascending the objects
print(list)
list.reverse()
print(list)
list.pop(7)#pop method use to remove what u declare the index#
print(list)
list.pop()#If u didn't declare the index it will remove from right element
print(list)