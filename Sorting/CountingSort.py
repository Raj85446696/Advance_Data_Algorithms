"""
Time Complexity 
Best Case = O(n+k)
Average Case = O(n+k)
Wrost Case = O(n+k)

Space Complexity 
O(n+k)
"""

def CountSort(arr):
    # Find max element
    maxx = arr[0]
    for i in range(len(arr)):
        if arr[i] > maxx:
            maxx = arr[i]
    
    # Initialize count array
    countArr = [0] * (maxx + 1)
    
    # Store frequency of each element
    for v in arr:
        countArr[v] += 1
    
    # Prefix sum to get positions
    for i in range(1, maxx + 1):
        countArr[i] += countArr[i - 1]
    
    # Build sorted array
    ans = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        v = arr[i]
        ans[countArr[v] - 1] = v
        countArr[v] -= 1
    
    # Copy sorted array back to original array
    for i in range(len(arr)):
        arr[i] = ans[i]


arr = [4, 2, 2, 8, 3, 3, 1]
CountSort(arr)
print(arr)
