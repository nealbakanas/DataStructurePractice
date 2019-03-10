class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)




class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        remove = self.items[0]
        self.items.remove(remove)
        return remove

    def __str__(self):
        return str(self.items)

queue1 = Queue()

queue1.push(1)
queue1.push(3)
queue1.push(5)
print (queue1)
queue1.pop()
print (queue1)
