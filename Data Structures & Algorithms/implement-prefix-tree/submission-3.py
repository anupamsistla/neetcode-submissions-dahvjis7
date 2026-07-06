class Node:
    def __init__(self, char):
        self.children = [None]*26
        self.char = char
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = Node("R")


    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c)-ord("a")
            if curr.children[index] != None:
                curr = curr.children[index]
            else:
                curr.children[index] = Node(c)
                curr = curr.children[index]
        
        curr.isWord = True

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
            index = ord(c)-ord("a")
            
            if curr.children[index] != None:
                curr = curr.children[index]
            
            else:
                return False
            
        return True
        