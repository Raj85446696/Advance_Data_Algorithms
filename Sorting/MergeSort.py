"""
Time Complexity 
Best Case = O(nlog(n))
Average Case = O(nlog(n))
Wrost Case = O(nlog(n))

Space Complexity 
O(n)
"""


def MergeSort(arr,left,right):
    if left<right:
        mid = left +(right-left)//2 
        MergeSort(arr,left,mid)
        MergeSort(arr,mid+1,right)
        Merge(arr,left,mid, right)
        
        
        
def Merge(arr,left,mid,right):
    n1 = mid-left+1
    n2 = right-mid
    arr1 = [0]*n1
    arr2 = [0]*n2
    
    
    # copy data to temp arr 
    for i in range(n1):
        arr1[i]=arr[left+i]
      
    for i in range(n2):
        arr2[i]=arr[mid+1+i]  
    
    
    # Copy back to original array 
    i = 0 
    j = 0 
    k = left 
    while(i<n1 and j<n2):
        if arr1[i]<=arr2[j]:
            arr[k] = arr1[i]
            i+=1 
        else: 
            arr[k] = arr2[j]
            j+=1 
        
        k+=1 
    
    
    while i<n1: 
        arr[k] = arr1[i]
        i+=1 
        k+=1 
    
    while j<n2:
        arr[k] = arr2[j]
        j+=1 
        k+=1
        
arr = [12, 9, 4, 5, 78, 90]
MergeSort(arr, 0, len(arr) - 1)
print(arr)
