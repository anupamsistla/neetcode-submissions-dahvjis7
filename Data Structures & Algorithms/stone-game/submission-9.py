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
        ahead = [0]*len(piles)

        for l in range(len(piles)-1, -1, -1):
            curr = [0]*len(piles)
            for r in range(l, len(piles)):
                even = True if (r-l) % 2 else False
                left = piles[l] if even else 0
                right = piles[r] if even else 0
            
                if l == r:
                    curr[r] = left
                
                else:
                    curr[r] = max(left + ahead[r], right + curr[r-1])
            ahead = curr
                
        aliceScore = ahead[len(piles)-1]
        return aliceScore > sum(piles) - aliceScore