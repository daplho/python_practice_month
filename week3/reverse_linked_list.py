import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next

        if node:
            fptr.write(sep)

def reverse(llist):
    if llist == None or llist.next == None:
        return llist
    
    prev_node = None
    cur_node = llist
    next_node = llist.next

    while cur_node != None:
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
        if next_node != None:
            next_node = next_node.next

    return prev_node

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()