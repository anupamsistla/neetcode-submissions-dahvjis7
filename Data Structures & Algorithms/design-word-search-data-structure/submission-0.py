class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TreeNode()
                curr = curr.children[c]
        
        curr.isWord = True
        return

    def search(self, word: str) -> bool:
        stack = [(self.root,0)]

        while stack:
            curr, index = stack.pop()
            if curr.isWord and index == len(word):
                return True
            if index < len(word):
                if word[index] in curr.children:
                    stack.append((curr.children[word[index]], index+1))


                elif word[index] == '.':
                    for value in curr.children.values():
                        stack.append((value, index+1))
        
        return False


# search:
# if c is a '.' I have to search every single tree/subtree starting from that node, searching node by node 