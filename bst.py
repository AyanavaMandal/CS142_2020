# https://en.wikipedia.org/wiki/Tree_(data_structure)
# https://en.wikipedia.org/wiki/Binary_tree 
# https://en.wikipedia.org/wiki/Binary_search_tree
# https://www.cs.rochester.edu/u/gildea/csc282/slides/C12-bst.pdf (Upto Page 20, rest will covered in CS301)

class Node:
    def __init__(self, val):
        self.data = val
        self.parent = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def searchU(self,val):
        self.search(val,self.root)
    def search(self,val,curr):
        if curr.data == val or curr is None:
            return curr
        elif val > curr.data:
            return self.search(val, curr.right)
        else:
            return self.search(val, curr.left)
    def insertU(self,val):
        # Case where BST is empty
        if self.root is None:
            temp = Node(val)
            self.root = temp
        else:
            self.insert(val,self.root)
    def insert(self,val,curr):
        #To go left or right
        if val > curr.data: #if right
            if curr.right is not None:
                self.insert(val,curr.right)
            else:
                temp = Node(val)
                curr.right = temp
                temp.parent = curr
        else: #If left
            if curr.left is not None:
                self.insert(val,curr.left) #Go to the left
            else:
                temp = Node(val) # Create a new node
                curr.left = temp # Insert yourself in left
                temp.parent = curr # Assign your parent
    def displayU(self):
        self.inOrder(self.root)
    def inOrder(self, curr):
        # left , center , right
        if curr:
            self.inOrder(curr.left)
            print(curr.data, end= ",")
            self.inOrder(curr.right)
    def findminU(self):
        if self.root:
            self.findmin(self.root)
    def findmin(self,curr):
        if curr.left is None:
            return curr
        else:
            return self.findmin(curr.left)
    #Find max
    def RIP(self, node1, node2):
        # Homework for replacement of root
        if node1:
            if node1.parent.right is node1:
                node1.parent.right = node2
            else:
                node1.parent.left = node2
        if node2:
            node2.parent = node1.parent
    '''
    def findsucc:
        findmin(curr.right

    def delete():
        loc = search(val)
        if two child
            # Find succ
            # Replace the value 
            # Delete the succ position 
        if one child 
            RIP (curr, curr.child)
        if no child 
            RIP (curr, None)
'''

bst1 = BST()
bst1.insertU(5)
bst1.insertU(2)
bst1.insertU(3)
bst1.insertU(1)
bst1.displayU()
