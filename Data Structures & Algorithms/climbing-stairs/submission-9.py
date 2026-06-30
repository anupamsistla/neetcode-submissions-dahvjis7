class Solution:
    def climbStairs(self, n):
        prev2, prev1 = 1, 1
        
        for i in range(2, n+1):
           temp = prev1
           prev1 = prev1 + prev2
           prev2 = temp
           
        return prev1