from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 
        visited = set()
        visited.add(0)

        i = 0
        queue = deque()
        queue.append(i)
        res = 0

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                for j in range(nums[curr]+1):
                    nextIndex = curr + j
                    
                    if nextIndex in range(len(nums)) and nextIndex not in visited:
                        queue.append(nextIndex)
                        visited.add(nextIndex)
            res += 1
        
        return res -1