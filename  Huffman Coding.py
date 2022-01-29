import sys


class MinHeap:
    def __init__(self):
        self.heap_arr = [None]
        self.currentSize = 0
    
    def heapify_up(self, i):
        while i // 2 > 0:
            if self.heap_arr[i] < self.heap_arr[i//2]:
                self.swap(i, i//2)
            i = i // 2
    
    def insert(self, value):
        self.heap_arr.append(value)
        self.currentSize += 1
        self.heapify_up(len(self.heap_arr) - 1)

    def min_child_index(self, i):
        left_child_index = 2*i
        right_child_index = left_child_index + 1
        if right_child_index > len(self.heap_arr) - 1:
            return left_child_index
        else:
            if self.heap_arr[left_child_index] < self.heap_arr[right_child_index]:
                return left_child_index
            else:
                return right_child_index
    
    def heapify_down(self, i):
        while 2*i <= len(self.heap_arr) - 1:
            min_child_i = self.min_child_index(i)
            if self.heap_arr[i] > self.heap_arr[min_child_i]:
                self.swap(i, min_child_i)
            i = min_child_i
    
    def extract_min(self):
        if self.currentSize > 0:
            self.swap(1, len(self.heap_arr) - 1)
            min = self.heap_arr.pop()
            self.currentSize -= 1
            self.heapify_down(1)
            return min
        return None
    
    def get_min(self):
        if self.currentSize > 0:
            return self.heap_arr[1]
        return None
    
    def size(self):
        return self.currentSize
    
    def swap(self, index, other_index):
        temp = self.heap_arr[index]
        self.heap_arr[index] = self.heap_arr[other_index]
        self.heap_arr[other_index] = temp


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def get_char(self):
        return self.char

    def get_frequency(self):
        return self.frequency

    def get_left(self):
        return self.left
    
    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right
    
    def set_right(self, node):
        self.right = node

    def __lt__(self, other):
        
        return self.frequency  < other.frequency

    def __eq__(self,other):
        return self.frequency == other.frequency

class HuffmanTree:
    def __init__(self, root):
        self.root = root
    
    def get_root(self):
        return self.root
    
    def build_encode_key(self):
        encode_key = {}
        def traverse(node, code):
            if node:
                if node.get_left():
                    traverse(node.get_left(), code + "0")
                if node.get_right():
                    traverse(node.get_right(), code + "1")
                if node.get_left() is None and node.get_right() is None: 
                    encode_key[node.get_char()] = code
        node = self.root
        if node:
            if node.get_left() is None and node.get_right() is None:
                encode_key[node.get_char()] = "0"
            else:
                traverse(node, "")
        return encode_key


def huffman_encoding(data):
    frequency_table = {}
    for c in data:
        frequency = frequency_table.get(c,0)
        if frequency:
            frequency_table[c] += 1
        else:
            frequency_table[c] = 1

    min_heap = MinHeap()
    for key in frequency_table:
        node = HuffmanNode(key, frequency_table[key])
        min_heap.insert(node)
    
    while min_heap.size() > 1:
        first_min = min_heap.extract_min()
        second_min = min_heap.extract_min()
        internal_node = HuffmanNode(None, first_min.frequency + second_min.frequency)
        internal_node.left = first_min
        internal_node.right = second_min
        min_heap.insert(internal_node)
    
    encoded_string = ""
    root = min_heap.get_min()
    huffman_tree = HuffmanTree(root)
    encode_key = huffman_tree.build_encode_key()
    for char in data:
        encoded_string += encode_key[char]
    return encoded_string, huffman_tree

def huffman_decoding(data,tree):
    decoded_string = ""

    if tree is None:
        return ""

    node = tree.get_root()

    for bit in data:
        if bit == "0":
            if node.get_left():
                node = node.get_left()
            if node.get_left() is None and node.get_right() is None:
                decoded_string += node.get_char()
                node = tree.get_root()
        elif bit == "1":
            if node.get_right():
                node = node.get_right()
            if node.get_left() is None and node.get_right() is None:
                decoded_string += node.get_char()
                node = tree.get_root()
    return decoded_string

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    sen = "aaaaa" #The content of the data is: aaaaa

    print ("The size of the data is: {}\n".format(sys.getsizeof(sen)))  #The size of the encoded data is: 24
    print ("The content of the data is: {}\n".format(sen)) #The content of the encoded data is: 00000

    encoded_data, tree = huffman_encoding(sen)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) #The size of the decoded data is: 54
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #The content of the encoded data is: aaaaa 
    print ("The content of the encoded data is: {}\n".format(decoded_data))



    