class Solution:
    def foo(self, i, alice, stoneValue, dp):
        if (i, alice) in dp:
            return dp[(i, alice)]
        
        if i == len(stoneValue):
            return 0
        
        if alice:
            maxRes = float("-inf")
            res = 0
            for j in range(0, 3):
                if (i + j) < len(stoneValue):
                    res += stoneValue[i+j]
                    maxRes = max(res + self.foo(i+j+1, False, stoneValue, dp), maxRes)
            dp[(i, alice)] = maxRes
            return maxRes
            
        else:
            minRes = float("inf")
            for j in range(0, 3):
                if (i + j) < len(stoneValue):
                    minRes = min(minRes, self.foo(i+j+1, True, stoneValue, dp))
            dp[(i, alice)] = minRes
            return minRes
    
                
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        aliceScore = self.foo(0, True, stoneValue, dp)
        sumValues = sum(stoneValue)
        bobScore = (sumValues - aliceScore) 

        if aliceScore > bobScore:
            return "Alice"
        
        elif aliceScore == bobScore:
            return "Tie"
        
        return "Bob"
    
        