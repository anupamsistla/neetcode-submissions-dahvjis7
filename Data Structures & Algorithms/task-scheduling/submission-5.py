class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        time = 0 
        q = deque()

        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1

            if maxHeap:
                res = 1 + heapq.heappop(maxHeap)
                if res:
                    q.append((res, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time