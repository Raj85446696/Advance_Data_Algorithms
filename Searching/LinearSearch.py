
"""
Time Complexity of Linear Search 
Best Case = 1 
Average Case = O(n)
Wrost Case = O(n)

Space Complexity id O(1)

"""
def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1 

arr = [23,45,76,12,3]
tar = 3
print(LinearSearch(arr,tar))