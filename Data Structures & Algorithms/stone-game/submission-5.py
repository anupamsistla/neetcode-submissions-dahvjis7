class Solution:
    def foo(self, l, r, piles, dp):
        if l > r:
            return 0
        
        if dp[l][r] != -1:
            return dp[l][r]
        
        even = True if (r-l) % 2 else False
        left = piles[l] if even else 0
        right = piles[r] if even else 0
    
        left = left + self.foo(l+1, r, piles, dp)
        right = right + self.foo(l, r-1, piles, dp)
        
        dp[l][r] = max(left, right)
        return dp[l][r]

    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[-1]*len(piles) for _ in range(len(piles))]
        aliceScore = self.foo(0, len(piles)-1, piles, dp)
        return aliceScore > sum(piles) - aliceScore