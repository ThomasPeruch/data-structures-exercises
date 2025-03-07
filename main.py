class Stack:
    def __init__(self):
        self.itens = []

    def push(self,item):
        self.itens.append(item)

    def pop(self):
        if len(self.itens) > 0:
            return self.itens.pop()
        else :
            return 'Lista Vazia'
    
    def peek(self):
        if len(self.itens) > 0:
            return self.itens[-1]
        else:
            return 'Lista Vazia'

def verifica_balanceamento(expressao):
    stack = Stack()

    for char in expressao:
        if char == "(":
           stack.push(char)
        elif char == ")":
            if len(stack.itens) == 0:
                return False
            stack.pop()
    return len(stack.itens) == 0

expressoes = [
    "(a + b) * (c + d)", 
    "(a + b * (c + d)",
    "((a + b) * c)",
    "((a + b)) * (c + d))",
    "(a + b)",
    "a + b * c - d",
]

for expressao in expressoes:
    print(f"'{expressao}': {verifica_balanceamento(expressao)}")
        

