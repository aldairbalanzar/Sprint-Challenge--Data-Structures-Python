"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
​
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
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
               self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
               self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

# Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        if self.value is None:
            return None
        if self.right:
            return self.right.get_max()

        return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value is None: 
            return None
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

        fn(self.value)

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return
        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print()
        # visit the node by printing its value
        print(self.value)
        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        # You should import the queue class from earlier in the
        from queue import Queue
        # we and use that class to implement this method
        # Use a queue to form a "line"
        q = Queue()
        # for the nodes to "get in"
        # start by placing the root in the queue
        q.enqueue(node)
        # need a while loop to iterate
        while q.size > 0:
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item
            current = q.dequeue()
            print(current.value)
        # place current item's left node in queue if not None
            if current.left:
                q.enqueue(current.left)
        # place current item's right node in queue if not None
            if current.right:
                q.enqueue(current.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal
    def dft_print(self, node):
        from stack import Stack
        s = Stack()
        s.push(node)
        while s.size > 0:
            current_node = s.pop()
            print(current_node.value)
            if current_node.left:
                s.push(current_node.left)
            if current_node.right:
                s.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
