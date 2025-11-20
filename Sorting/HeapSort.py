"""
Time Complexity 
Best Case = O(nlog(n))
Average Case = O(nlog(n))
Wrost Case = O(nlog(n))

Space Complexity 
O(1)
"""

def heapSort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move max to end
        heapify(arr, i, 0)  # heapify reduced heap


def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
arr = [12, 9, 4, 5, 78, 90]
heapSort(arr)
print(arr)
