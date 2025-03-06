class Stack:
    def __init__(self):
        self.itens = []

    def push(self,item):
        self.append(item)

    def pop(self):
        if not len(self.itens) > 0:
            return self.itens.pop()
        else :
            return 'Lista Vazia'
    
    def peek(self, item):
        if not self.itens.isEmpty():
            return self.itens[-1]
        else:
            return 'Lista Vazia'

stack = Stack()