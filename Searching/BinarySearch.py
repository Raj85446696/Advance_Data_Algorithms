"""
Time Complexity of binary Search 
Best Case = 1 
Average Case = O(logn)
Wrost Case = O(logn)

Space Complexity id O(1)

"""

def BinarySearch(arr,target):
    left = 0 
    right = len(arr)
    while left<=right:
        mid = left+(right-left)//2 
        if arr[mid]==target:
            return mid 
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid-1 
        
    return -1 


arr = [1,2,3,4,5,6,7,8]
tar = 6
print(BinarySearch(arr,tar))
            