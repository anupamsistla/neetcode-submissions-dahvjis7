from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = defaultdict(list)
        visited = set()

        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                key = ""
                for k in range(len(wordList[i])):
                    if j == k:
                        key += "*"
                    else:
                        key+=wordList[i][k]

                newKey = tuple(key)

                edges[newKey].append(wordList[i])

        queue = deque()
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

                    newKey = tuple(key)

                    for nei in edges[newKey]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            count += 1
        return 0


            