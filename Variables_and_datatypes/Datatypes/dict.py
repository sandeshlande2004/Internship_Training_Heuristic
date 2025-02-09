# **DICTONARY**

dict = {'name': 'M S Dhoni', 
        'age': 39, 
        'team': 'CSK', 
        'runs': 4500,
        'wickets': 0,
        'matches': 204}
print(dict)
print(dict['name']) #indexing of dictionary
print(dict['age'])
dict['wickets'] = 7 #overwrite the value of dictionary
print(dict)
print(dict.keys()) #keys of dictionary
print(dict.values()) #values of dictionary
print(dict.items()) #items of dictionary
print(dict.get('name')) #get the value of dictionary
dict.update({'team': 'MI'}) #update the value of dictionary
print(dict)
dict.pop('matches') #pop the value from dictionary
print(dict)
dict.popitem() #pop the last item from dictionary
print(dict)
dict.clear() #clear the dictionary
print(dict)

dict1 = {'name': 'Virat',
        'age': 32,
        'team': 'RCB',
        'runs': 5800,
        'wickets': 0,
        'matches': 180}
print(dict1)
print(dict.update(dict1)) #update the dictionary dict with dict1
print(dict)
