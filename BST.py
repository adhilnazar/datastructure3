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


def is_identical(r1,r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    
    return (r1.key == r2.key) and\
            is_identical(r1.left,r2.left) and\
            is_identical(r1.right,r2.right)  

def closest_val(root,target):
    closest = root.key
    while root:
        closest = min(root.key,closest, key=lambda x: abs(target - x))

        if target < root.key:
            root = root.left
        elif target > root.key:
            root = root.right
        else:
            return root.key
    return closest

b = BST(None)
list1 = [-1,15,10,17,16,8,11,16,18]
for i in list1:
    b.insert(i)

# c = BST(None)
# list2 = [15,10,17,16,8,11,16,18,9]
# for i in list2:
#     c.insert(i)

# print(is_identical(b,c))
target = 14
result = closest_val(b,target)
print(f"the closest value of {target} is : {result}")