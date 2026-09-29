class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)

        for a, b in prerequisites:
            adjList[b].append(a)
        
        prereqMap = {}

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for preq in adjList[crs]:
                    prereqMap[crs] |= dfs(preq)
                prereqMap[crs].add(crs)
            
            return prereqMap[crs]


        for i in range(numCourses):
            dfs(i)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        
        return res 


