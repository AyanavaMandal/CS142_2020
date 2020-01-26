'''
https://en.wikipedia.org/wiki/Priority_queue

A priority queue must at least support the following operations:

is_empty: check whether the queue has no elements.
insert_with_priority: add an element to the queue with an associated priority.
pull_highest_priority_element: remove the element from the queue that has the highest priority, and return it.

https://en.wikipedia.org/wiki/Binary_heap

A binary heap is defined as a binary tree with two additional constraints:[3]

Shape property: a binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
Heap property: the key stored in each node is either greater than or equal to (≥) or less than or equal to (≤) the keys in the node's children, according to some total order.


'''

class Bheap:
    def __init__(self):
        self.ilist = []
        self.index = 0

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def insert(self, val):
        self.ilist.append(val)
        self.index = self.index + 1
        i = self.index - 1
        while i is not 0:
            if self.ilist[self.parent(i)] > self.ilist[i]:
                self.ilist[self.parent(i)], self.ilist[i] = self.ilist[i], self.ilist[self.parent(i)]
                i = self.parent(i)
            else:
                break
    def display(self):
        print(self.ilist)
bh = Bheap()
bh.insert(6)
bh.insert(5)
bh.insert(4)
bh.insert(3)
bh.insert(2)
bh.insert(1)
bh.display()
