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
        self.right_child= right_child

    def __lt__(self, second):
        return self.frequency < second.frequency

    def __str__(self):
        return "character: {}  frequency: {} \n".format(self.character,
                                                                self.frequency)


class Tree:

    def __init__(self, text):
        if len(text) == 0:
            return
        
        frequency = {i : text.count(i) for i in set(text)}
        self.priority_queue = [Node(key, value) for key, value in frequency.items()]
        heapify(self.priority_queue)
        print(self)

        while len(self.priority_queue) != 1:
            r_child = heappop(self.priority_queue)
            l_child = heappop(self.priority_queue)
            frequency_sum = r_child.frequency + l_child.frequency
            new_node = Node(None, frequency_sum, left_child=l_child, right_child=r_child)
            heappush(self.priority_queue, new_node)


    def encode():
        pass


    def decode():
        pass


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

###################
    input_text = "huffman xxxxxxxxxxx"
    mystring = list_to_str(input_text)
    print("Input: {}".format(mystring))

    tree = Tree(mystring)

####################
    if not os.path.isfile('./{}'.format(OUTPUT_FILE)):
        os.mknod("{}".format(OUTPUT_FILE))

    output_file = open("./{}".format(OUTPUT_FILE), 'w')
    output_file.write("hello world")
    output_file.close()
    print("\n")
