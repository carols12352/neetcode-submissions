class TreeNode:
    def __init__(self):
        self.child = {}
        self.isend = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.child:
                node.child[ch] = TreeNode()
            node = node.child[ch]

        node.isend = True


    def _find(self, word: str):
        node = self.root

        for ch in word:
            if ch not in node.child:
                return None
            node = node.child[ch]
        return node
        
    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.isend

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        
        