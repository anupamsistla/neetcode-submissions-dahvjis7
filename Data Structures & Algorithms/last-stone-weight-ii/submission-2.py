class Solution:
    def foo(self, i, target, stones, dp):
        if dp[i][target] != -1:
            return dp[i][target]
        if i == 0:
            return stones[0] if stones[0] <= target else 0
        
        notTake = self.foo(i-1, target, stones, dp)
        take = float("-inf")
        if stones[i] <= target:
            take = stones[i] + self.foo(i-1, target-stones[i], stones, dp)
        
        dp[i][target] = max(notTake, take)
        return dp[i][target]

    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStones = sum(stones)
        n = len(stones)
        midWay = sumStones//2

        dp = [[-1] * (midWay+1) for _ in range(n)]
        
        bag2 = self.foo(n-1, sumStones//2, stones, dp)
        bag1 = sumStones - bag2
        return bag1 - bag2
        

        