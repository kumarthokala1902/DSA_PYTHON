# constructor for Doubly linked list
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedlist():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # To append values for the list

    def append_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    # def pop_last(self):
    #     temp = self.tail
    #     if self.length == 0:
    #         return None
    #     self.tail = temp.prev
    #     self.tail.next = None
    #     temp.prev = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp.value

    # to methods of pop_last element
    def pop_last(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    # to remove first element fro the list
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # to add elements at beginning of the list

    def prepend_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return self.head

    # To print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = DoublyLinkedlist(2)
my_list.print_list()

print(my_list.pop_first())

my_list.print_list()
