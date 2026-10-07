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
        ahead = [0] * len(piles)
        
        for l in range(len(piles)-1, -1, -1):
            curr = [0] * len(piles)
            for r in range(l, len(piles)):
                if l == r:
                    continue
                
                even = True if (r-l) % 2 else False

                if even:
                    curr[r] = max(piles[l] + ahead[r], piles[r] + curr[r-1])
                 
                else:
                    curr[r] = min(ahead[r], curr[r-1])  
            ahead = curr

        aliceScore = ahead[len(piles)-1]
        return aliceScore > sum(piles) - aliceScore        