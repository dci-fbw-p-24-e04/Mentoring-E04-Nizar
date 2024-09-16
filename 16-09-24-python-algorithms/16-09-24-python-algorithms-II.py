from collections import Counter
# we need to find the duplicated elements in this list
list_of_items = ['a','w','e','a','b','m','m']
def get_duplicates(list):
    counter = Counter(list)#is counting the number of occuence of an element in a list
    #counter = {'a': 2, 'm': 2, 'w': 1, 'e': 1, 'b': 1}
    s = []
    for c in counter.keys():
        if counter[c]>1:
            s.append(c)
            
    return s

print(get_duplicates(list_of_items))
#christian solution 
def get_duplicates(lst: list):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

print(get_duplicates(list_of_items))

#Noah solution
list_of_items = ["a", "w", "e", "a", "b", "m", "m"]

def find_duplicates(list):
    duplicates = []
    for i in list:
        if i in list[list.index(i)+1:] and i not in duplicates:
            duplicates.append(i)
    return duplicates

print(find_duplicates(list_of_items))

#if we want to remove all the duplicated elements 

def remove_duplicates(items):
    #because sets do not allow duplicates
    return list(set(items))

print(remove_duplicates(list_of_items))