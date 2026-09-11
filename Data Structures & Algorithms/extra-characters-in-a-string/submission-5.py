class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            
            curr.isWord = True
        return

class Solution:
    def foo(self, i, s, words, dp, root):
        if i == len(s):
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        res = 1 + self.foo(i+1, s, words, dp, root)
        curr = root

        for j in range(i, len(s)):
            if not s[j] in curr.children:
                break
            curr = curr.children[s[j]]

            if curr.isWord:
                res = min(res, self.foo(j+1, s, words, dp, root))
        
        dp[i] = res
        return res

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)
        root = trie.root

        words = set(dictionary)
        dp = [-1]*len(s)

        return self.foo(0, s, words, dp, root)
