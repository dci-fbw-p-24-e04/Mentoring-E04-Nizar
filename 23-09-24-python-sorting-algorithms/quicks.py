

def quick_sort(arr):
    #base case 
    if len(arr)<2:
        return arr
    
    low,same,high = [],[],[]
    pivot = arr[len(arr)//2]#we choose the middle one
    
    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
            
    return quick_sort(low) + same + quick_sort(high)

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90,72]
    sorted_arr = quick_sort(arr)
    print("Sorted array is:", sorted_arr)