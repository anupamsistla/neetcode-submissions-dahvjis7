class Solution:
    def foo(self, l, r, piles, dp):
        if l > r:
            return 0
        
        if dp[l][r] != -1:
            return dp[l][r]
        
        even = True if (r-l) % 2 else False

        if even:
            dp[l][r] = max(piles[l] + self.foo(l+1, r, piles, dp), piles[r] + self.foo(l, r-1, piles, dp))
            return dp[l][r]
        
        dp[l][r] = min(self.foo(l+1, r, piles, dp), self.foo(l, r-1, piles, dp))
        return dp[l][r]
        
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for l in range(len(piles)-1, -1, -1):
            for r in range(l, len(piles)):
                even = True if (r-l) % 2 else False

                if l == r:
                    continue

                if even:
                    dp[l][r] = max(piles[l] + dp[l+1][r], piles[r] + dp[l][r-1])
            
                else:    
                    dp[l][r] = min(dp[l+1][r], dp[l][r-1])
                

        aliceScore = dp[0][len(piles)-1]
        
        return aliceScore > sum(piles) - aliceScore
    
        