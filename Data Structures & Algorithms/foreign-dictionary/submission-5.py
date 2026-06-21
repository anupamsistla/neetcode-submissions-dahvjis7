from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for w in words for c in w}
        inDegree = {c: 0 for w in words for c in w}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        
        visited = set()
        queue = deque()

        for _, values in adjList.items():
            for v in values:
                inDegree[v] += 1

        for k in inDegree.keys():
            if inDegree[k] == 0:
                queue.append(k)
                visited.add(k)
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            
            for v in adjList[curr]:
                inDegree[v] -= 1

                if inDegree[v] == 0:
                    queue.append(v)
                    visited.add(v)
        
        for k in inDegree.keys():
            if inDegree[k] == 0 and k not in visited:
                res.append(k)
                visited.add(k)
    
        return "".join(res) if len(visited) == len(inDegree.keys()) else ""