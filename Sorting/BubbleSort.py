"""
Time Complexity 
Best Case = O(n2)
Average Case = O(n2)
Wrost Case = O(n2)

Space Complexity 
O(1)
"""

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                

arr = [12,9,4,5,78,90]
BubbleSort(arr)
print(arr)