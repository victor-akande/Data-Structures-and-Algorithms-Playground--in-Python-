class BST:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child= None

    # Insertion operation
    def insert(self, data):
        # Check is the tree is empty and insert data into the node
        if self.key is None:
            self.key = data
            return
        # Check if the data is less than that of the root node
        if self.key > data:
            # If there is existing data in the left child, recursively call the insert method
            if self.left_child:
                self.left_child.insert(data)
            # If no data exists, create a new node then insert the data into the left child
            else:
                self.left_child = BST(data)  
        # Run if the data is greater than that of the root node
        elif self.key < data:
            # Recursively call the insert method if there is existing data in the right child
            if self.right_child:
                self.right_child.insert(data)
            # Create a new node and then insert data into the right child
            else:
                self.right_child = BST(data)
        else:
            return data
        
    def search(self, data):
        if self.key == data:
            print("Node found! ->", data)
            return
        
        if data < self.key:
            if self.left_child:
                self.left_child.search(data)
            else:
                print("Node is not present in the tree!")
        elif data > self.key:
            if self.right_child:
                self.right_child.search(data)
            else:
                print("Node is not present in the tree! ")

    def preorder(self):
        # Visit root node
        print(self.key, end="->")
        # Check if left child is present
        if self.left_child:
            # Visit right sub-tree (recursively)
            self.left_child.preorder()
        # Check if right child is present
        if self.right_child:
            # Visit right sub-tree (recursively)
            self.right_child.preorder()

    def inorder(self):
        # Check if left child is present
        if self.left_child:
            # Visit the left subtree (recursively)
            self.left_child.inorder()
        # Visit the root node
        print(self.key, end="->")
        # Check if right child is present
        if self.right_child:
            # Visit right sub-tree (recursively)
            self.right_child.inorder()

    def postorder(self):
        # Check if left child is present
        if self.left_child:
            # Visit the left subtree (recursively)
            self.left_child.postorder()
        # Check if right child is present
        if self.right_child:
            # Visit right sub-tree (recursively)
            self.right_child.postorder()
        # Visit the root node
        print(self.key, end="->")

    def delete(self, data):
        absent_node_msg = "Given Node is not present in the tree"
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.left_child:
                self.left_child = self.left_child.delete(data)
            else:
                print(absent_node_msg)
        if data > self.key:
            if self.right_child:
                self.right_child = self.right_child.delete(data)
            else: 
                print(absent_node_msg)
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            if self.right_child is None:
                temp = self.right_child
                self = None
                return temp
            node = self.right_child
            while node.left_child:
                node = node.left_child
            self.key = node.key
            self.right_child = self.right_child.delete(node.key)
        

        


root_node = BST(100)
items = [23, 15, 29, 45, 123, 65, 140, 174]
items = [52, 93, 15, 72, 61, 21, 83, 87, 75, 75, 88, 100, 24, 3, 22, 53, 2, 88, 30, 38, 2, 64, 60, 21, 33, 76, 58, 22, 89, 49, 91, 59, 42, 92, 60, 80, 15, 62, 62, 47, 62, 51, 55, 64, 3, 51, 7, 21, 73, 39, 18, 4, 89, 60, 14, 9, 90, 53, 2, 84, 92, 60, 71, 44, 8, 47, 35, 78, 81, 36, 50, 4, 2, 6, 54, 4, 54, 93, 63, 18, 90, 44, 34, 74, 62, 100, 14, 95, 48, 15, 72, 78, 87, 62, 40, 85, 80, 82, 53, 24]
# To add a list (or an types of iterable) of nodes to the BST
for item in items:
    root_node.insert(item)
# To search the BST for using list (or an types of iterable)
for item in items:
    root_node.search(item)

print("\nPre-order")
root_node.preorder()
print("\nIn-order")
root_node.inorder()
print("\nPost-order")
root_node.postorder()
print("\n")