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
        


root_node = BST(100)
items = [23, 15, 23, 45, 123, 65, 140, 174]
# To add a list (or an types of iterable) of nodes to the BST
for item in items:
    root_node.insert(item)
