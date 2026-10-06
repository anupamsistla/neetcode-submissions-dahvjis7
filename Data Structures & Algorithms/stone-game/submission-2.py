class Solution:
    def foo(self, i, alice, piles, dp):
        if dp[i][alice] != -1:
            return dp[i][alice]

        if i == 0:
            if alice:
                return piles[0]
            else:
                return -piles[0]
            
        if alice:
            left = piles[0] + self.foo(i-1, False, piles[1:], dp)
            right = piles[-1] + self.foo(i-1, False, piles[:len(piles)-1], dp)
        
        else:
            left = -piles[0] + self.foo(i-1, True, piles[1:], dp)
            right = -piles[-1] + self.foo(i-1, True, piles[:len(piles)-1], dp)   

        dp[i][alice] = max(left, right)
        return dp[i][alice]

    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[-1] * 2 for _ in range(len(piles))]
        score = self.foo(len(piles)-1, True, piles, dp)
        
        return score > 0
        