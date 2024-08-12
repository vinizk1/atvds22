class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)- 1]
    
    def size(self):
        return len(self.items)
    
pilhaCopos = Stack()

#Para fins de comparação, estamo em o boteco os copo estão sujos de whisky e a cada copo tomado, o garçon leva o copo sujo.

pilhaCopos.push('Copo 1')
pilhaCopos.push('Copo 2')
pilhaCopos.push('Copo 3')
print(pilhaCopos.items)

#Após o primeiro gole
print(pilhaCopos.peek())
pilhaCopos.pop()
print(pilhaCopos.items)

#Após o segundo gole
print(pilhaCopos.peek())
pilhaCopos.pop()
print(pilhaCopos.items)

#Após o terceiro gole
print(pilhaCopos.peek())
pilhaCopos.pop()
print(pilhaCopos.items)


lista = []