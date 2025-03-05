class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None  # basic constructor od the bst

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node  # inserts root as an new_node if the root is empty
            return True
        temp = self.root
        while True:
            if temp.value == new_node:
                return False
            if new_node.value < temp.value:
                if temp.left is None:  # inserting the value at left position if the value is less then the root
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if new_node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_node  # inserting the value at right position if the value is greater then the root
                        return True
                    temp = temp.right

    def contain_val(self, value):               # to check the wether the value contains the tree or not.
        temp = self.root
        if self.root == None:
            return "The tree is empty"

        while temp is not None:
            if value<temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False








my_bst = Bst()
#
# for val in [3, 4, 2]:
#     my_bst.insert(val)



print(my_bst.contain_val(24))
