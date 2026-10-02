import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        visited = set()
        neighbors = [[0, 1], [0, -1], [1, 0], [-1,0]]
        
        while pq:
            effort, currI, currJ = heapq.heappop(pq)
            
            if currI == len(heights)-1 and currJ == len(heights[0])-1:
                return effort

            if (currI, currJ) in visited:
                continue
            
            visited.add((currI, currJ))

            for stepI, stepJ in neighbors:
                newI, newJ = currI + stepI, currJ + stepJ
                
                if newI in range(len(heights)) and newJ in range(len(heights[0])) and (newI, newJ) not in visited:
                    currEffort = max(effort, abs(heights[newI][newJ] - heights[currI][currJ]))
                    heapq.heappush(pq, (currEffort, newI, newJ))
        
        return effort
        

                
        