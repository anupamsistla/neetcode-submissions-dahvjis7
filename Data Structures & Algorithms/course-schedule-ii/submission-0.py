from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        inDegree = dict()

        for a, b in prerequisites:
            edges[b].append(a)
            inDegree[a] = 1 + inDegree.get(a, 0)

        for i in range(numCourses):
            if i not in inDegree:
                inDegree[i] = 0
        
        queue = deque()
        for i in range(numCourses):
            if i in inDegree and inDegree[i] == 0:
                queue.append(i)

        res = []
        count = 0
        while queue:
            curr = queue.popleft()
            res.append(curr)
            count+= 1

            for nei in edges[curr]:
                inDegree[nei] -= 1

                if inDegree[nei] == 0:
                    queue.append(nei)
        
        print(count)
        if count != numCourses:
            return []

        return res

        
        