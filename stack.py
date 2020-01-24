class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Mystack:
    def __init__(self):
        self.top = None
    def push(self,value):
        item = Node(value)
        item.next = self.top
        self.top = item
    def pop(self):
        if self.top == None:
            print("No items in stack to pop")
        else:
            self.top = self.top.next
    def display(self):
        if self.top != None:
            print("The top is ",self.top.data)
        else:
            print("No items in the linkedlist")

s1 = Mystack()
s1.push(1)
s1.push(2)
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()