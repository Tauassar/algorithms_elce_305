import copy


class HuffmanTree:
    # first node of the tree
    root = None
    # actual value stored in node
    key = None
    value = None
    code =''
    codes_list = []
    # children of the node
    left = None
    right = None
    # parent node
    p = None

    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val

    # return key and value when called on print or converted to string
    def __str__(self):
        return "{0}:{1}".format(self.key, self.value)

    def print_codes(self, type):
        print('\n')
        print(f'Codes for {type} codeword:')
        self.in_order_tree_walk(self.root)
        size = 0
        for [code, freq] in self.codes_list:
            size += len(code) * freq
        print(f"\nSize of the compressed file after encoding using {type} coding: {size}")
        return self.codes_list

    # actual algorithm of inorder tree walk presented in lectures
    def in_order_tree_walk(self, node, code_append=''):
        if code_append is not None:
            node.code += code_append
        if node.left is not None:
            self.in_order_tree_walk(node.left, node.code+'0')
        if node.key is not None:
            self.codes_list.append([node.code, node.value])
            print('{0}: {1}'.format(node.key, node.code), end='\t')
        if node.right is not None:
            self.in_order_tree_walk(node.right, node.code+'1')


class MinPriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        # for checking if the queue is empty
        return len(self.queue) == 0

    def insert(self, data):
        # for inserting an element in the queue
        self.queue.append(data)

    def pop(self):
        # for popping an element based on Priority
        try:
            min_queue = 0
            for i in range(len(self.queue)):
                if self.queue[i].value < self.queue[min_queue].value:
                    min_queue = i
            item = self.queue[min_queue]
            del self.queue[min_queue]
            return item
        except IndexError:
            print('error')


def count_chars(string):
    char_frequency = {}
    for char in set(string):
        char_frequency[char] = string.count(char)
    return char_frequency


def huffman_variable(char_queue):
    for i in range(len(char_queue) - 1):
        node = HuffmanTree()
        x = char_queue.pop()
        node.left = x
        y = char_queue.pop()
        node.right = y
        node.value = x.value + y.value
        char_queue.insert(node)
    root = char_queue.pop()
    root.root = root
    return root


def huffman_fixed(char_queue):
    secondary_queue = MinPriorityQueue()
    for i in range(len(char_queue) - 1):
        try:
            node = HuffmanTree()
            x = char_queue.pop()
            node.left = x
            y = char_queue.pop()
            node.right = y
            node.value = x.value + y.value
            secondary_queue.insert(node)
        except:
            continue
    for j in range(len(secondary_queue) - 1):
        node = HuffmanTree()
        x = secondary_queue.pop()
        node.left = x
        y = secondary_queue.pop()
        node.right = y
        node.value = x.value + y.value
        secondary_queue.insert(node)
    root = secondary_queue.pop()
    root.root = root
    return root


def main():
    file = open('Input.txt', 'r')
    file_string = file.read()
    # file_string = "BCAADDDCCACACAC"
    char_set = count_chars(file_string)
    variable_queue = MinPriorityQueue()
    fixed_list = []
    for k, v in char_set.items():
        variable_queue.insert(
            HuffmanTree(key=k, val=v)
        )
        fixed_list.append(
            HuffmanTree(key=k, val=v)
        )
    print("\nInitial values: {0}".format(variable_queue))
    print("Actual number of bits: {0}".format(len(file_string)*8), end='')

    root_fixed = huffman_fixed(fixed_list)
    root_fixed.print_codes('Fixed-length')

    root_variable = huffman_variable(variable_queue)
    root_variable.print_codes('Variable-length')


if __name__ == "__main__":
    main()
