class Solution:
    def foo(self, i, M, alice, piles, dp):
        if i == len(piles):
            return 0
        
        if (i, M, alice) in dp:
            return dp[(i, M, alice)]
        
        res = 0 if alice else float("inf")
        total = 0
        
        for X in range(0, 2*M):
            if i + X > len(piles)-1:
                break
                
            total += piles[i + X]
            
            if alice:
                res = max(res, total + self.foo(i+X+1, max(X+1, M), False, piles, dp))
            
            else:
                res = min(res, self.foo(i+X+1, max(X+1, M), True, piles, dp))
        
        dp[(i, M, alice)] = res
        return res

    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        return self.foo(0, True, 1, piles, dp)
        