class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sumStones = sum(stones)
        midWay = sumStones // 2
        dp = [[0]*(midWay+1) for _ in range(len(stones))]

        for target in range(midWay + 1):
            if stones[0] <= target:
                dp[0][target] = stones[0]

        for i in range(1, len(stones)):
            for target in range(midWay+1):
                notTake = dp[i-1][target]
                take = float("-inf")

                if stones[i] <= target:
                    take = stones[i] + dp[i-1][target - stones[i]]
                
                dp[i][target] = max(notTake, take)

        bag2 = dp[n-1][midWay]
        bag1 = sumStones - bag2
        return bag1 - bag2
        