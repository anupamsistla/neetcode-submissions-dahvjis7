from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque()
        queue.append((0, 0))
        visited = set()

        while queue:
            i, currJump = queue.popleft()

            for j in range(i+1, min(i + nums[i] + 1, len(nums))):
                if j == len(nums)-1:
                    return currJump + 1
                if j not in visited:
                    queue.append((j, currJump+1))
                    visited.add(j)

        return 0
