class Queue:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0) 
        return 'Fila vazia'

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        return 'Fila vazia'

    def is_empty(self):
        return len(self.itens) == 0

def printing(documents):
    queue = Queue()

    priorities_values = {'Low': 5, 'Medium': 3, 'High': 1}

    print('Receiving documents...\n')

    for document in documents:
        queue.enqueue(document)

    while not queue.is_empty() :
        doc = queue.dequeue()

        for i in range(priorities_values[doc['priority']], 0, -1):
            print(f'printing in {i}')
        print(f"{doc['name']} printed\n")

    print("Printer's Queue is Empty")

documents = [
    {'name': 'Annual Sales Report 2024','priority': 'Medium'},
    {'name': 'Payroll 25/01', 'priority':'High'}, 
    {'name': 'New Vendor Presentation', 'priority': 'Low'},
    {'name': 'Internship Program Presentation', 'priority': 'Medium'},
    {'name': 'Data Traffic in Marketplace 2024 Q4','priority': 'Medium'},
    {'name': 'Stock Flutuation','priority': 'Medium'},
    {'name': 'Vacation Document', 'priority': 'High'}
]

printing(documents)
