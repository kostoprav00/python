# Закодируйте любую строку по алгоритму Хаффмана.


from collections import *
import operator

text = 'it is a beautiful day'


class Node:
    def __init__(self, value: str, frequency: int, left=None, right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.code = 'N/A'
        self.right = right

    def __repr__(self):
        return f'["{self.value}": frequency: {self.frequency} code: {self.code}]'

    def is_leaf(self):
        return self.left is None and self.right is None

    def sort_nodes_by_freq(input_list: list) -> list:
        return sorted(input_list, key=lambda x: x.frequency)


class Tree:
    def __init__(self):
        self.root = None

    def print_all_children(self, node, code: str):
        if node.is_leaf():
            node.code = code
            print(node)
            return
        self.print_all_children(node.left, code + '1')
        self.print_all_children(node.right, code + '0')


def get_counter(input_text: str) -> dict:
    counter = dict()
    text_array = deque(input_text)
    for i in text_array:
        curr_val = counter.get(i, 0)
        counter[i] = curr_val + 1
    return counter


def dict_to_list(unsorted_dict: dict) -> list:
    unsorted_list = list()
    for freq in unsorted_dict.items():
        unsorted_list.append(Node(freq[0], freq[1]))
    return unsorted_list


def get_tree(input_list: list) -> Node:
    input_list = Node.sort_nodes_by_freq(input_list)
    left = input_list.pop(0)
    right = input_list.pop(0)
    current_node = Node('node', left.frequency + right.frequency)
    current_node.left = left
    current_node.right = right
    input_list.append(current_node)
    if len(input_list) == 1:
        return current_node
    return get_tree(input_list)


init_frequent = get_counter(text)
print(init_frequent)
list_initial = dict_to_list(init_frequent)

t = Tree()
t.root = get_tree(list_initial)
t.print_all_children(t.root, '')
