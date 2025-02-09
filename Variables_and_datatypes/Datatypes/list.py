list3 = [1, 2, 3, 'a', 'a', 'b', 12]

list3.append(5) # To add any new element in list

list3.remove('b') # To remove any element from list

print(list3[6]) # To print any element from list by usint its index value

print(list3)

#  ** LIST**
list = ['a',12, 'raghav', 45.99, 'true']
print(list)
print(list[0]) #indexing of list
print(list[1:3]) #slicing of list
list.append('new') #append new element to list
print(list)
list[2] = 'viraj' #overwrite element of list
print(list)
list.remove('true') #remove element from list
print(list)
list.pop() #remove last element from list
print(list)
list.pop(1) #remove element from specific index
print(list)
list.insert(1, 'new') #insert element at specific index
print(list)
list.reverse() #reverse the list
print(list)

list1 = [10,45,9,2,3,6,7,8,1]
list1.sort() #sort the list
print(list1)

print(list+list1) #concatenation of two lists