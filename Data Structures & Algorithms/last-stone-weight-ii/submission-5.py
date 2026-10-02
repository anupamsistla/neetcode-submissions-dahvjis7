class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sumStones = sum(stones)
        midWay = sumStones // 2
        prev = [0]*(midWay+1)

        for target in range(midWay + 1):
            if stones[0] <= target:
                prev[target] = stones[0]

        for i in range(1, len(stones)):
            curr = [0]*(midWay+1)
            for target in range(midWay+1):
                notTake = prev[target]
                take = float("-inf")

                if stones[i] <= target:
                    take = stones[i] + prev[target - stones[i]]
                
                curr[target] = max(notTake, take)
            prev = curr

        bag2 = prev[midWay]
        bag1 = sumStones - bag2
        return bag1 - bag2
        