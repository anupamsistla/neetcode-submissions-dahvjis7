class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        lastOccurance = {}

        minRes = float("inf")
        for i in range(len(cards)-1, -1, -1):
            if cards[i] in lastOccurance:
                toPick = lastOccurance[cards[i]] - i + 1
                
                if toPick != 1:
                    minRes = min(minRes, toPick)
            
            lastOccurance[cards[i]] = i
        
        return minRes if minRes != float("inf") else -1