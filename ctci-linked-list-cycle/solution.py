"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not isinstance(head, Node):
        return False
    rabbit, turtle = head, head
    while True:
        if not rabbit.next or not rabbit.next.next:
            return False
        rabbit = rabbit.next.next
        turtle = turtle.next
        if turtle == rabbit:
            return True
            
    
