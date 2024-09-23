


def bubble_sort(lst):
    n = len(lst)
    swapped = False # to check if the two elements are swapped or not
    for i in range(0,n-1):
        
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                swapped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped:
            break

    return lst
    
    
if __name__ == '__main__':
    arr = [11, 12, 22, 25, 34, 64, 72, 90,100]
    sorted_arr = bubble_sort(arr)
    print("Sorted array is:", sorted_arr)