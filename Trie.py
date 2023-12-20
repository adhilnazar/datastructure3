class TrieNode:
    def __init__(self) -> None:
        self.children = dict()
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,data):    
        node = self.root
        for char in data:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def Search(self,data):
        node = self.root
        for char in data:
            if char not in node.children:
                return False
            node = node.children[char]
        return True