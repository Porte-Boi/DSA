class BinarySearchTreeNode:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        if val< self.left:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    # find min
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    # find max
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max() 


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    number = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(number)
    print(number_tree.in_order())
    print(f"Min; {number_tree.find_min()}")
    print(f"Max; {number_tree.find_max()}")

