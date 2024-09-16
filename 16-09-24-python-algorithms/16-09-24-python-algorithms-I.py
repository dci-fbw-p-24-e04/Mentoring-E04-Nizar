# i want to check if the string is palindrome or not

def is_rec_palindrome(string):# the recusrsive way to check if the string is palindrome or not
    if len(string) <= 1:
        return True
    if string[0]==string[-1]:
        return is_rec_palindrome(string[1:-1])
    else :
        return False
    
#or we can do it in a simpler way
def is_palindrome(string):
    return string == string[::-1]

#let say that you have a list of numbers and a target number
# you have to find the two numbers that their sum is equal to the target number
#[1,4,10,7,8,9] target = 13
print('-'*50)
sorted_list = [1,3,4,7,8,8,11,13,19,31]
target = 18
def get_sum(list,target):#O(n^2) double loops
    for i in range(len(list)-1):
        for j in range (i+1,len(list)-1):   
            if list[i]+list[j] == target:
                return list[i],list[j]
    return None

print(get_sum(sorted_list,target))
print('-'*50)
def get_sum_2(list,target):
    for i in list:
        if target-i in list:
            return i,target-i
print(get_sum_2(sorted_list,target))
print('-'*50)
sorted_list = [1,3,4,7,8,8,11,13,19,31]
target = 100
#algorithm optimisation
def get_sum_3(list,target):#O(n)
    l = 0
    r = len(list)-1
    while l<r:
        if list[l]+list[r]<target:
            l=l+1
        elif list[l]+list[r]>target:
            r=r-1
        else : #list[l]+list[r]==target 
            return list[l],list[r]
    return None

print(get_sum_3(sorted_list,target))