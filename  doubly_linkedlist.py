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

    def pop_last(self):
        temp = self.tail
        if self.length == 0:
            return None
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # method two of pop_last element
    def pop_last_method2(self):
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

    # to remove first element for the list
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

    def get_index(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next

            return temp.value

    def get_method2(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp

    # function to change the value in the specified index
    def set_value(self, index, value):
        temp = self.get_method2(index)
        if temp:  # it will conform's that hte temp is not none
            temp.value = value
            return True
        return False

    # function to insert element at any position
    def insert_element(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend_value(value)
        if index == self.length:
            return self.append_value(value)

        else:
            new_node = Node(value)
            before = self.get_method2(index - 1)
            after = before.next
            before.next = new_node
            new_node.prev = before
            new_node.next = after
            after.prev = new_node

            self.length += 1
            return True

    # method1 to remove element from any position
    def remove_element(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop_last_method2()

        else:
            temp = self.get_method2(index)

            before = temp.prev
            after = temp.next

            before.next = after
            after.prev = before
            temp.next = None
            temp.prev = None
            self.length -= 0

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    # method2 to remove element from any list
    def remove_method2(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop_last_method2()

        else:
            temp = self.get_method2(index)

            temp.next.prev = temp.prev
            temp.prev.next = temp.next

            temp.next = None
            temp.prev = None

            self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value


# class and function calling here
#                 <---------->

my_list = DoublyLinkedlist(0)
for value in [2, 3, 4, 5, 6, 7, 2, 8]:
    my_list.append_value(value)

print(f" the popped item is <- {my_list.remove_method2(7)} ->", '\n')
# my_list.insert_element(0, 14)
my_list.print_list()




                                                                                                # kumar reddy