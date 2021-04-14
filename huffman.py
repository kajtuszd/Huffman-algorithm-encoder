import os
from heapq import heappop, heappush, heapify


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


class Node:
    
    def __init__(self, character, frequency, left_child=None, 
                                                            right_child=None):
        self.character = character
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child

    def __lt__(self, second):
        return self.frequency < second.frequency

    def __str__(self):
        return "character: {}  frequency: {} \n".format(self.character,
                                                                self.frequency)
    
    def has_no_children(self):
        return self.left_child is None and self.right_child is None



class Tree:

    def __init__(self, data):
        self.data = data
        frequency = {i : data.count(i) for i in list(self.data)}
        self.priority_queue = [Node(key, value) for key, value in frequency.items()]
        # print(self) # uncomment to see each character frequency

    
    def compute(self):
        heapify(self.priority_queue)
        while len(self.priority_queue) != 1:
            r_child = heappop(self.priority_queue)
            l_child = heappop(self.priority_queue)
            frequency_sum = r_child.frequency + l_child.frequency
            new_node = Node(None, frequency_sum, left_child=l_child, right_child=r_child)
            heappush(self.priority_queue, new_node)

        codes = {}
        Tree.encode(self.priority_queue[0], "", codes)
        # print("Codes: {}\n".format(codes)) # uncomment to see each letter in binary
        encoded_text = ""

        for character in self.data:
            encoded_text += codes.get(character)

        # print("Encoded text: {} \n".format(encoded_text)) # uncomment to see encoded text
        print("Decoded text: ", end="")

        if self.priority_queue[0].has_no_children():
            while self.priority_queue[0].frequency > 0:
                print(self.priority_queue[0].character, end='')
                self.priority_queue[0].frequency -= 1
        else:
            index = -1
            while index < len(encoded_text) - 1:
                index = Tree.decode(self.priority_queue[0], index, encoded_text)
        return encoded_text


    @staticmethod
    def encode(top, encoded_text, code):
        if top is None:
            return

        if top.has_no_children():
            code[top.character] = encoded_text if len(encoded_text) > 0 else '1'

        Tree.encode(top.left_child, encoded_text + '0', code)
        Tree.encode(top.right_child, encoded_text + '1', code)


    @staticmethod
    def decode(top, pointer, encoded_text):
        if top is None:
            return pointer

        if top.has_no_children():
            print(top.character, end='')
            return pointer
        
        pointer += 1
        top = top.left_child if encoded_text[pointer] == '0' else top.right_child
        return Tree.decode(top, pointer, encoded_text)


    def __str__(self):
        nodes_text = ""
        for node in self.priority_queue:
            nodes_text += node.__str__()
        return nodes_text



def list_to_str(array):
    text = ""
    for element in array:
        text += element
    return text


if __name__ == '__main__':

    if not os.path.isfile('./{}'.format(INPUT_FILE)):
        os.mknod("{}".format(INPUT_FILE))
        raise Exception("Type text to be encoded in {}".format(INPUT_FILE))

    if not os.path.getsize("./{}".format(INPUT_FILE)):
        raise Exception("{} is empty".format(INPUT_FILE))

    input_text = []
    with open('./{}'.format(INPUT_FILE)) as input_file:
        input_text = input_file.readlines()

    text = list_to_str(input_text)
    # print("Input: {} \n".format(text)) # uncomment to see input

    tree = Tree(text)
    encoded_text = tree.compute()

    if not os.path.isfile('./{}'.format(OUTPUT_FILE)):
        os.mknod("{}".format(OUTPUT_FILE))

    output_file = open("./{}".format(OUTPUT_FILE), 'w')
    output_file.write(encoded_text)
    output_file.close()
    print("\n")
