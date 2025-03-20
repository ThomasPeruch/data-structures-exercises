class Node:
    def __init__(self, value):
        self.value = value 
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        #insertion in linkedlist
        if self.head:
            pointer = self.head
            while pointer.next_node :
                pointer = pointer.next_node
            node = Node(value)
            pointer.next_node = node
        else:
            #first insertion in linkedlist
            self.head = Node(value)

    def print_list(self):
        if self.head:
            pointer = self.head
            while pointer.next_node:
                print(pointer.value,end=" ! ")
                pointer = pointer.next_node
        else:
            print('lista vazia')

linkedList = LinkedList()
linkedList.push(2)
linkedList.print_list()

linkedList.push(3)
linkedList.push(5)
linkedList.print_list()

