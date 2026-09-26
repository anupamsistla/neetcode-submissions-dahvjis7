class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)

        if totalCost > totalGas:
            return -1
        
        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]

            if total < 0:
                total = 0
                res = i + 1
        return res