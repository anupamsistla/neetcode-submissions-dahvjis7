import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []

        countChars = defaultdict(int)

        for c in s:
            countChars[c] += 1
    
        for c in countChars:
            heapq.heappush(maxHeap, (-countChars[c], c))

        res = []
        prev = None
        while maxHeap:
            count, curr = heapq.heappop(maxHeap)

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if res and res[-1] == curr:
                if len(maxHeap) == 0:
                    return ""
                else:
                    prev = (count, curr)

            else:
                res.append(curr)
                count += 1

                if count < 0:
                    heapq.heappush(maxHeap, (count, curr))


        return "".join(res)        

