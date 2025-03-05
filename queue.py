class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        if temp == None:
            return "The queue is empty!"
        else:
            while temp:
                print(temp.value)
                temp = temp.next

        print(self.last.next)

    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        temp = self.first
        if temp is None:
            return "no more value to remove"
        else:
            self.first = temp.next
            # temp = None
        self.length -= 1
        return f"the returned value is {temp.value}"



my_queue = Queue(90)
my_queue.enqueue(20)

for value in range():
    my_queue.enqueue(value)

print(my_queue.dequeue())

my_queue.print_queue()
