# Doubly Linked List Code
class Item:
    def __init__(self, val):
        self.val = val
        self.nex = None
        self.pre = None

class DLinkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,val):
        # Create a new item 
        newItem = Item(val)
        newItem.nex = self.head
        if self.head is not None:
            self.head.pre = newItem
        self.head = newItem
    
    def insertAtEnd(self,val):
        newItem = Item(val)
        if self.head is None:
            self.insertAtBegin(val)
        else:
            curr = self.head
            while curr.nex is not None:
                curr = curr.nex
            curr.nex = newItem
            newItem.pre = curr
    
    
    def display(self):
        curr = self.head
        while curr != None: 
            print(str(curr.val)+"->",end = '')
            curr = curr.nex
        print("None")

# Create an object of class linkedlist
ll1  = DLinkedlist()
ll1.insertAtEnd(0)
ll1.insertAtBegin(1)
ll1.insertAtBegin(2)
ll1.insertAtBegin(3)
ll1.insertAtEnd(-1)
ll1.display()