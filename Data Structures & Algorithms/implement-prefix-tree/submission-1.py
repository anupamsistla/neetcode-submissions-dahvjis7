class TreeNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index] != None:
                curr = curr.children[index]
            else:
                curr.children[index] = TreeNode()
                curr = curr.children[index]
        curr.isWord = True
        return

    def search(self, word: str) -> bool:
        curr = self.root 
        
        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index] != None:
                curr = curr.children[index]
            else:
                return False
            
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            index = ord(c) - ord("a")

            if curr.children[index] != None:
                curr = curr.children[index]
            else:
                return False

        return True        