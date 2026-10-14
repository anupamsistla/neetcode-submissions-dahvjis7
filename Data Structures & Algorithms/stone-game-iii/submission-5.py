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
        
        n = len(stoneValue)
        dp[(n, True)] = 0
        dp[(n, False)] = 0

        aliceRange = [False, True]

        for i in range(n-1, -1, -1):
            for alice in aliceRange:
                if alice:
                    maxRes = float("-inf")
                    res = 0
                    for j in range(0, 3):
                        if (i + j) < len(stoneValue):
                            res += stoneValue[i+j]
                            maxRes = max(maxRes, res + dp[(i+j+1, False)])
                    dp[(i, alice)] = maxRes
                
                else:
                    minRes = float("inf")
                    for j in range(0, 3):
                        if (i + j) < len(stoneValue):
                            minRes = min(minRes, dp[(i+j+1, True)])
                    dp[(i, alice)] = minRes


        aliceScore = dp[(0, True)]
        sumValues = sum(stoneValue)
        bobScore = (sumValues - aliceScore) 

        if aliceScore > bobScore:
            return "Alice"
        
        elif aliceScore == bobScore:
            return "Tie"
        
        return "Bob"
    
        