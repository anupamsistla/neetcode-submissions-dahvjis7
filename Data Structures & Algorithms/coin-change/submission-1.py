class Solution:
    def foo(self, i, target, coins, dp):
        if i == 0:
            if target % coins[0] == 0:
                return target // coins[0]
            
            else:
                return float("inf")
        
        if dp[i][target] != -1:
            return dp[i][target]
        
        notTake = self.foo(i-1, target, coins, dp)
        take = float("inf")
        if coins[i] <= target:
            take = 1 + self.foo(i, target - coins[i], coins, dp)

        dp[i][target] = min(notTake, take)
        return dp[i][target]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        prev = [0] * (amount+1)

        for target in range(0, amount+1):
            if target % coins[0] == 0:
                prev[target] = target // coins[0]
            else:
                prev[target] = float("inf")

        for i in range(1, n):
            curr = [0] * (amount+1)
            for target in range(0, amount+1):
                notTake = prev[target]
                
                take = float("inf")
                if coins[i] <= target:
                    take = 1 + curr[target - coins[i]]

                curr[target] = min(notTake, take)
            prev = curr

        toRet = prev[amount]

        return toRet if toRet != float("inf") else -1