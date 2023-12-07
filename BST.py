class BST:
    def __init__(self,data) -> None:
        self.key = data
        self.left = None
        self.right = None

    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        
        elif self.key < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
        
        else:
            self.key = data

    # def Delete(self,data):
    #     if self.key is None:
    #         print("Tree is Empty")
    #         return
    #     if self.key > data:
    #         if self.left:
    #             self.left = self.left.Delete(data)
    #         else:
    #             print("Node is not in the tree")
    #     elif self.key < data:
    #         if self.right:
    #             self.right = self.right.Delete(data)
    #         else:
    #             print("Node is not in the tree")
    #     else:
    #         if self.left is None:
    #             temp = self.right
    #             self = None
    #             return temp
    #         if self.right is None:
    #             temp = self.left
    #             self = None
    #             return temp
    #         node = self.left
    #         while self.right:
    #             node = self.right
    #         self.key = node.key
    #         self.left = self.left.Delete(node.key)
    #     return self
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key,end=" ")
        if self.right:
            self.right.in_order()
    
    def pre_order(self):
        print(self.key,end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key,end=" ")
    def search(self,data):
        if self.key == data:
            print("Node Found")
            return
        if self.key > data:
            if self.left:
                self.left.search(data)
            else:
                print("Node not in this Tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node not in this Tree")
    def Delete(self,data):
        if self.key is None:
            return
        if self.key > data:
            if self.left:
                self.left = self.left.Delete(data)
            else:
                print("Node not in this BST")
        elif self.key < data:
            if self.right:
                self.right = self.right.Delete(data)
            else:
                print("Node not in this BST")

        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.left
            while self.right:
                node = self.right
            self.key = node.key
            self.left = self.left.Delete(node.key)
        return self 
        
b = BST(None)
list1 = [15,10,17,16,8,11,16,18]
for i in list1:
    b.insert(i)
b.in_order()
print("After Deletion\n")
b. Delete(0)
# b.in_order()
b.post_order()
print("\n")
b.search(15)