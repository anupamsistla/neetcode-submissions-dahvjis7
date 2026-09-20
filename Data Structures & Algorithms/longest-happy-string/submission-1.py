class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [] 
        
        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))

        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))
        
        res = ""
        while maxHeap:
            count, curr = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == curr:
                if not maxHeap:
                    break
                
                count2, curr2 = heapq.heappop(maxHeap)
                res += curr2
                count2 += 1

                if count2 != 0:
                    heapq.heappush(maxHeap, (count2, curr2))
                
                res += curr
                count += 1

                if count != 0:
                    heapq.heappush(maxHeap, (count, curr))
            
            else:
                res += curr
                count += 1
                
                if count != 0:
                    heapq.heappush(maxHeap, (count, curr))
        
        return res