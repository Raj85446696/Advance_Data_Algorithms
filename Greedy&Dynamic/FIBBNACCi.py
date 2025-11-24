# TC = O(2^n) SC =O(n)
# def Fibbnacci(n):
#     if n<=1:
#         return n 
#     return Fibbnacci(n-1)+Fibbnacci(n-2)


# Optimal Approch
# TC = O(n) SC =O(1)
def Fibbnacci(n):
    if n<=1 : 
        return n 
    a,b = 0 , 1 
    for i in range(2,n+1):
        sum = a+b 
        a = b 
        b = sum
    return sum 


# DP Tabularization 
# TC = O(n) SC =O(n)
# def Fibbnacci(n):
#     if n<=1:
#         return n 
    
#     dp = [0]*(n+1)
#     dp[0] = 0 
#     dp[1] = 1 
#     for i in range(2,n+1):
#         dp[i] = dp[i-1]+dp[i-2]
    
#     return dp[n]

# DP Memorization
# TC = O(n) SC =O(n)
# def Fibbnacci(n,dp=None):
#     dp = [-1]*(n+1)
#     if n<=1:
#         return n 

#     if dp[n]!=-1:
#         return dp[n]
#     dp[n] = Fibbnacci(n-1,dp)+Fibbnacci(n-2,dp)
#     return dp[n]


n = 6
print(Fibbnacci(n))


