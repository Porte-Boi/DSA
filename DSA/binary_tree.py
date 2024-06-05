class BinarySearchTreenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # Add data in the left subtree.
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreenode(data)
        else:
            # Add data in the right subtree.
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreenode(data)

    def in_order_traversal(self):
        elements = []

        # Visit left tree.
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Visit the base node.
        elements.append(self.data)

        # Visit right tree.
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    # Used for searching
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
     # find Min
    def find_min(self):
            
        if self.left is None:
            return self.data
        return self.left.find_min()
        
    # find max
    def find_max(self):
            
         if self.right is None:
             return self.data
         return self.right.find_max()
        
     # delete functions
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val >self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            max_val = self.left.find_max()
            self.data = max_val

            self.left = self.left.delete(max_val)

        return self
                

def build_tree (elements):
    root = BinarySearchTreenode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

    

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    
    numbers_tree.delete(1)
    print(numbers_tree.in_order_traversal())