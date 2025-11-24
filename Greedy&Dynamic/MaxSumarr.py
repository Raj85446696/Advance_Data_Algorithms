def MaxSubArray(nums):
    maxSum = nums[0]
    currSum = 0 
    for n in nums:
        currSum+=n 
        maxSum = max(maxSum,currSum)

        if currSum<0:
            currSum=0
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(MaxSubArray(nums))