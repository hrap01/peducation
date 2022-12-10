from typing import Optional

#strom je repreyovan7 rooutem
class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def insert_node(self, value_added: int):
        if value_added < self.value:
            if self.left is not None:
                self.left.insert_node(value_added)
            else:
                self.left = Node(value_added)
        elif value_added == self.value:
            pass
        else:
            if self.right is not None:
                self.right.insert_node(value_added)
            else:
                self.right = Node(value_added)

    def __repr__(self):
        return f'({self.value})'


root_node = Node(value=5)
root_node.insert_node(8)
root_node.insert_node(7)

print(root_node.right.left.right)