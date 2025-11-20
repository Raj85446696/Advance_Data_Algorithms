"""
Time Complexity 
Best Case = O(n2)
Average Case = O(n2)
Wrost Case = O(n2)

Space Complexity 
O(1)
"""

def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        minidx = i
        for j in range(i+1,n):
            if arr[j]<arr[minidx]:
                minidx = j 
        arr[i],arr[minidx] = arr[minidx], arr[i]




arr = [12,9,4,5,78,90]
SelectionSort(arr)
print(arr)