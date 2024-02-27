from typing import Self


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next: Self = next

    def toList(self) -> list:
        lst = [self.val]
        t = self
        while t.next:
            lst.append(t.next.val)
            t = t.next
        return lst


def deleteVal(node: Node, val) -> Node:
    root = node
    prev = root
    while prev.next:
        t = prev.next
        if t.val == val:
            prev.next = t.next
        prev = t
    return root


node = Node(1, Node(2, Node(6, Node(3, Node(4, Node(5, Node(6)))))))
print(node.toList())

node = deleteVal(node, 6)
print(node.toList())
