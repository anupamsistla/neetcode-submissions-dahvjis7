class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-2], cost[-1]

        for i in range(len(cost)-3, -1, -1):
            temp = one
            one = min(one, two) + cost[i]
            two = temp
        
        return min(one, two)