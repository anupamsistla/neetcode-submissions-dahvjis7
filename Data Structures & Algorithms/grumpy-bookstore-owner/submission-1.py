class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        currSatis = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                currSatis += customers[i]
        
        l,r = 0, 0
        maxSatis = currSatis
        extraSatis = 0
        while r < len(grumpy):
            if grumpy[r] == 1:
                extraSatis += customers[r]
                maxSatis = max(maxSatis, currSatis + extraSatis)
            
            if r-l+1 == minutes:
                if grumpy[l] == 1:
                    extraSatis -= customers[l]
                l+= 1
                
            r += 1
        
        return maxSatis
