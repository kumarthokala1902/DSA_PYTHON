# creating a constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# assigning the values to the linked list
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # append function to add elements to a linked list
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # popping out the elements from the existing list
    def pop_element(self):
        if self.length == 0:
            return "no elements in list"
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # adding elements at the starting of the linked list
    def prepend_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:

            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # function to pop the first element in the list
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value

    # print the list off all elements
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # function to get the value at teh expected index from the linked list
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # set method used to replace the elements by its existing value to a new value
    # set method uses the get method to find the index of te value
    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove_element(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            print(self.pop_first())
        elif index == self.length - 1:
            temp = self.get_value(index - 1)
            temp = self.tail
            temp.next = None
            return temp.value
        else:
            prev = self.get_value(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp.value

    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.pop_element()
my_list.pop_element()
my_list.print_list()
