class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start from the station that has the least cost but enough gas to cover the jounrey
        if sum(cost) > sum(gas):
            return -1
        
        res = 0
        total = 0

        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]

            if total < 0:
                res = i + 1
                total = 0
        
        return res