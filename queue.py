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
