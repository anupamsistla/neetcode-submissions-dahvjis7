class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        vals = [-cnt for cnt in count.values()]
        heapq.heapify(vals)
        q = deque()
        
        time = 0
        while vals or q:
            if q:
                if q[0][1] == time:
                    heapq.heappush(vals, q.popleft()[0])
            if vals:
                res = 1 + heapq.heappop(vals)
                if res:
                    q.append((res, time + n + 1))
        
            time += 1
        return time
            