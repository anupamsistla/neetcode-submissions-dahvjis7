from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = defaultdict(list)
        queue = deque()

        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                key = ""

                for k in range(len(wordList[i])):
                    if j == k:
                        key += "*"
                    
                    else:
                        key += wordList[i][k]
                
                key = tuple(key)
                edges[key].append(wordList[i])
        
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        count = 1

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                
                if curr == endWord:
                    return count

                for j in range(len(curr)):
                    key = ""
                    
                    for k in range(len(curr)):
                        if j == k:
                            key += "*"
                        else:
                            key += curr[k]

                    key = tuple(key)
                    for nei in edges[key]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            count += 1
        return 0