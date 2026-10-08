class Solution:
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