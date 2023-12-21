def heapify(arr,n,index):

    largest = index
    left = (2*index)+1
    right = (2*index)+2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index],arr[largest] = arr[largest],arr[index]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    for i in range((n-1)//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        self.end = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            return True 
        
list1 = [5,6,8,7,9,4,2,3,1]
n = len(list1)
heap_sort(list1)
print(list1)