"""
Time Complexity 
Best Case = O(nlog(n))
Average Case = O(nlog(n))
Wrost Case = O(n2)

Space Complexity 
O(log(n))
"""

def QuickSort(arr,left,right):
    if(left<right):
        pivot = pivotIndex(arr,left,right)
        QuickSort(arr,left,pivot-1)
        QuickSort(arr,pivot+1,right)
        
        
        
def pivotIndex(arr,left,right):
    
    # select pivot index 
    pivot = arr[right]
    i = left-1
    
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1 
            arr[i],arr[j] = arr[j] , arr[i]
    arr[i+1],arr[right] = arr[right] , arr[i+1]
    
    return i+1 

arr = [12, 9, 4, 5, 78, 90]
QuickSort(arr, 0, len(arr)-1)
print(arr)

    