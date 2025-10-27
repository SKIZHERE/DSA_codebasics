class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

    def in_order_traversal(self):
        elements = []
        # left side first
        if self.left:
            elements += self.left.in_order_traversal()
        #main node
        elements.append(self.data)
        #right node
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self,val):
        if val == self.data:
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

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:len(elements)]:
        root.add_child(element)
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,24]
    tree = build_tree(numbers)
    tree.delete(20)
    print("after deleting 20",tree.in_order_traversal())