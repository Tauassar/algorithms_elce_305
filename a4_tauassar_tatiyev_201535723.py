# Binary tree from previous assignment
class HuffmanTree:
    # first node of the tree
    root = None
    # actual value stored in node
    key = None
    value = None
    code = ''
    codes_list = []
    # children of the node
    left = None
    right = None

    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.code = ''
        self.codes_list = []
        self.left = None
        self.right = None

    # return key and value when called on print or converted to string
    def __str__(self):
        return "{0}:{1}".format(self.key, self.value)

    # prints codes saved inside a tree
    # calculates size of huffman coded file
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
    # generates codes for branches in binary search tree
    # and saves them into node's code variable and root's
    # code_list list
    def in_order_tree_walk(self, node, code_append=''):
        if code_append is not None:
            node.code += code_append
        if node.left is not None:
            self.in_order_tree_walk(node.left, node.code + '0')
        if node.key is not None:
            self.codes_list.append([node.code, node.value])
            print('{0}: {1}'.format(node.key, node.code), end='\t')
        if node.right is not None:
            self.in_order_tree_walk(node.right, node.code + '1')


# minimum priority queue
# code is taken from internet and slightly changed for current needs
# code referenced from https://www.geeksforgeeks.org/priority-queue-in-python/
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
        # for popping an element based on minimum Priority
        # i.e. pops element with minimum value
        try:
            min_queue = 0
            for i in range(len(self.queue)):
                if self.queue[i].value < self.queue[min_queue].value:
                    min_queue = i
            item = self.queue[min_queue]
            del self.queue[min_queue]
            return item
        except IndexError:
            print('Index out of range')


# counts unique characters using python set in a given string
def count_chars(string):
    char_frequency = {}
    for char in set(string):
        char_frequency[char] = string.count(char)
    return char_frequency


def huffman_variable(char_queue):
    insert_node(char_queue, char_queue)
    # pop root value
    root = char_queue.pop()
    root.root = root
    # print codes
    root.print_codes('Variable-length')
    return root


def huffman_fixed(char_queue):
    secondary_queue = MinPriorityQueue()
    insert_node(char_queue, secondary_queue)
    insert_node(secondary_queue, secondary_queue)
    root = secondary_queue.pop()
    root.root = root
    # print code
    root.print_codes('Fixed-length')
    return root


def insert_node(queue_1, queue_2):
    # insert node into a tree
    for i in range(len(queue_1) - 1):
        try:
            node = HuffmanTree()
            x = queue_1.pop()
            node.left = x
            y = queue_1.pop()
            node.right = y
            node.value = x.value + y.value
            queue_2.insert(node)
        except Exception as e:
            continue


def main():
    # open input file
    file = open('Input.txt', 'r')
    # read values from file and put them into string
    file_string = file.read()
    # additional string to test variable length codeword
    # since input file does not properly test this feature
    # file_string = "BCAADDDCCACACAC"
    # count unique symbols
    char_set = count_chars(file_string)
    variable_queue = MinPriorityQueue()
    fixed_list = []
    # insert unique chars to list(for fixed) and queue(for variable)
    for k, v in char_set.items():
        variable_queue.insert(
            HuffmanTree(key=k, val=v)
        )
        fixed_list.append(
            HuffmanTree(key=k, val=v)
        )
    # print initial values
    print("\nInitial values: {0}".format(variable_queue))
    # print size without coding
    print("Actual number of bits: {0}".format(len(file_string) * 8), end='')
    # variable coding
    root_variable = huffman_variable(variable_queue)
    # fixed coding
    root_fixed = huffman_fixed(fixed_list)


if __name__ == "__main__":
    main()
