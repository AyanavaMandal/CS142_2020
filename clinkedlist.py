# Circular Linked List Code
class Item:
    def __init__(self, val):
        self.val = val
        self.next = None

class CLinkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,val):
        # Create a new item
        newItem = Item(val)
        curr = self.head
        
        newItem.next = self.head
        
        # Point the last element to the new Item
        if self.head != None:
            while curr.next != self.head:
                curr = curr.next
            curr.next = newItem
        else:
            newItem.next = newItem
        self.head = newItem

    def display(self):
        curr = self.head
        if self.head is not None:
            while curr.next != self.head: 
                print(str(curr.val)+"->",end = '')
                curr = curr.next
            print(str(curr.val)+"->",end = '')
        print("None")
        
# Create an object of class linkedlist
ll1  = CLinkedlist()
ll1.insertAtBegin(1)
ll1.insertAtBegin(2)
ll1.insertAtBegin(3)
ll1.display()