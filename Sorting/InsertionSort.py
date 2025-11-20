"""
Time Complexity 
Best Case = O(n)
Average Case = O(n2)
Wrost Case = O(n2)

Space Complexity 
O(1)
"""

def InsertionSort(arr):
    n = len(arr)
    
    for i in range(n):
        key = arr[i]
        j = i-1 
        while j>=0 and arr[j]>key: 
            arr[j+1] = arr[j]
            j-=1      
        arr[j+1] = key 
        
arr = [12, 9, 4, 5, 78, 90]
InsertionSort(arr)
print(arr)
