class TreeNode:

    def __init__(self, currChar):
        self.children = {}
        self.isWord = False
        self.currChar = currChar

class PrefixTree:

    def __init__(self):
        self.root = TreeNode("R")
        # insert a number1 for indicating that it is a word

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TreeNode(c)
                curr = curr.children[c]

        curr.isWord = True

            


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        
        return curr.isWord


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        
        return True
        
        