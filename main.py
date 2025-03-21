class Node:
    def __init__(self, value):
        self.value = value 
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        #insertion in linkedlist
        if self.head:
            pointer = self.head
            while pointer.next_node :
                pointer = pointer.next_node
            node = Node(value)
            pointer.next_node = node
            self.tail = node
        else:
            #first insertion in linkedlist
            self.head = Node(value)

    def print_list(self):
        if self.head:
            pointer = self.head
            while pointer.next_node:
                print(pointer.value,end=" -> ")
                pointer = pointer.next_node
            print(f"{pointer.value} -> {pointer.next_node}")
            print(f"Head : {self.head.value}")
            if self.tail:
                print(f"Tail: {self.tail.value}")
            else : 
                print(f"Tail: None") 
        else:
            print('lista vazia')
    
    def reverse_list(self):
        if self.head and self.tail:
            pointer = self.head
            previous_pointer = None
            while pointer.next_node:
                next = pointer.next_node
                pointer.next_node = previous_pointer
                previous_pointer = pointer
                pointer = next
            pointer.next_node = previous_pointer
            new_tail = self.head
            new_head = self.tail
            self.head = new_head
            self.tail = new_tail
            self.print_list()
        else:
            print("Impossivel prosseguir, lista vazia")


linkedList = LinkedList()
linkedList.push(2)
linkedList.push(3)
linkedList.push(5)
linkedList.push(23)
linkedList.push(34)
linkedList.push(76)
linkedList.push(9)
linkedList.push(45)
linkedList.print_list()
linkedList.reverse_list()
