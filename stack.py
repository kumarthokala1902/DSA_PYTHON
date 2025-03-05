class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        # print(self.height)

    def push_method(self, value):
        temp = self.top
        new_node = Node(value)
        if temp is None:
            self.top = new_node

        else:
            self.top = new_node
            new_node.next = temp
        self.height += 1

    def pop_top(self):
        temp = self.top
        if temp is None:
            return "No value to pop"
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return f"the removed value is {temp.value}"

    # def reverse(self):
    #     new_str = ""
    #     while self.top:
    #         new_str += self.pop_top
    #     return new_str




s = Stack(1)
for i in [23, 43, 45, 23, 3]:
    s.push_method(i)

# print(s.pop_top())
# print(s.pop_top())
# # s.push_method(3)
print(s.reverse())
s.print_list()
