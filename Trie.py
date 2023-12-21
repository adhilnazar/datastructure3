class TrieNode:
    def __init__(self) -> None:
        self.children = dict()
        self.endofword = False
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,data):    
        node = self.root
        for char in data:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        self.endofword = True

    def Search(self,data):
        node = self.root
        for char in data:
            if char not in node.children:
                return False
            node = node.children[char]
        return True