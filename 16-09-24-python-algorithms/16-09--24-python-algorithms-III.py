#searchings
import random
list_of_nums= list(range(1,1500))#this is a sorted list
target = random.randint(250,2000)
print(target)
def search(list,num):#linear
    for i in list:
        if num == i:
            return True
    return False
print(search(list_of_nums,target))
print(target)
def binary_search(list,num):#logarithmic
    left = 0
    right = len(list)-1
    while left<=right:
        mid = left + (right-left)//2 #middle eflement of the list
        if list[mid] == num:
            return True
        elif list[mid] < num:
            left = mid + 1
        elif list[mid] > num:
            right = mid - 1
        
        
    return False
print(binary_search(list_of_nums,target))
