"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self

        while (value < current.value and current.left 
            or value > current.value and current.right):
            if value < current.value:
                current = current.left
            else:
                current = current.right
        
        if value < current.value:
            current.left = BSTNode(value)
        else:
            current.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Root is self
        if self.value == target:
            return True

        if target < self.value:
            # Go left
            left_result = self.left and self.left.contains(target)
            return left_result
        else:
            right_result = self.right and self.right.contains(target)
            return right_result

    # Return the maximum value found in the tree
    def get_max(self):
        current = self

        while current.right:
            current = current.right
        
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        
        print(node.value)
        
        if node.right:
            node.right.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)