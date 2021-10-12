# Comment it before submitting


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return f"{self.next_item}-{self.value}"


def solution(node, idx) -> Node:
    def get_node_by_index(head, index):
        while index > 0:
            head = head.next_item
            index -= 1
        return head

    previous_node = get_node_by_index(node, idx - 1)
    next_node = get_node_by_index(node, idx + 1)
    if next_node:
        if idx == 0:
            return next_node
        else:
            previous_node.next_item = next_node
    else:
        previous_node.next_item = None

    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    print(new_head)
    # result is node0 -> node2 -> node3
