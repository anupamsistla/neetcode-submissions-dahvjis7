from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)

        inDegree = dict()

        for a, b in prerequisites:
            edges[b].append(a)
            inDegree[a] = 1 + inDegree.get(a, 0)
        
        # enqueue all vertices that do not have an incoming edge
        queue = deque()
        for i in range(numCourses):
            if i not in inDegree:
                inDegree[i] = 0
                queue.append(i)

        count = 0
        while queue:
            curr = queue.popleft()
            count += 1

            for nei in edges[curr]:
                inDegree[nei] -= 1

                if inDegree[nei] == 0:
                    queue.append(nei)
        
        print(count)
        return count == numCourses
            