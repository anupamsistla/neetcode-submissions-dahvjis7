class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        time = 0

        vals = [-cnt for cnt in count.values()]

        heapq.heapify(vals) 

        while vals or q:
            time += 1

            if vals:
                res = 1 + heapq.heappop(vals)
                if res:
                    q.append((res, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(vals, q.popleft()[0])

        return time