class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

def printLinkedList(head):
    while head != None:
        print(head.data)
        head = head.next

def reverse(head):
    if head.next == None:
        return head
    
    cur_head = reverse(head.next)
    head.next.next = head
    return cur_head

reversed_list = reverse(Node('a', Node('b', Node('c', None))))
printLinkedList(reversed_list)