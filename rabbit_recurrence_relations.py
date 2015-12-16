#!/usr/bin/python
#J.HE
#Desp.:
class Solution(object):
  @profile
  def totalRabbits( self, n, k ):
    # n monthes
    # k: each pair give birth to k rabbit pairs

    if n <= 2 : 
      return 1 
    ## first try
    # # # rabbit paris liveing for each month
    # dp = [ 0 for _ in range(n) ] 
    # dp[0] = 1
    # dp[1] = 1
    # for i in range(2, n) :
    #   dp[i] = k * dp[i-2] + dp[i-1] 

    ## optimize memory 
    dp = [1,1]
    i = 2
    while i < n :
	curr =  k * dp[0] + dp[1] 
	dp = [dp[1], curr]
	i += 1
    return curr 

sol = Solution()
# print sol.totalRabbits(5, 3 ) 
print sol.totalRabbits(35, 5 ) 


