# Time Complexity  = O(2^n) and Space complexity = O(n)

def SubsetProblem(arr,n,target):
    if target==0:
        return True 
    
    if n==0:
        return False
    
    if arr[n-1]>target:
        return SubsetProblem(arr,n-1,target)
    
    return SubsetProblem(arr,n-1,target-arr[n-1]) or SubsetProblem(arr,n-1,target)

arr = [3,34,4,19,5,2]
print(SubsetProblem(arr,len(arr),10))