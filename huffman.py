import os

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
        return "character: {}  frequency: {}".format(self.character,
                                                                self.frequency)

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
    node = Node('a', 32)
    print(node)

    mystring = list_to_str(input_text)
    print(mystring)


####################
    if not os.path.isfile('./{}'.format(OUTPUT_FILE)):
        os.mknod("{}".format(OUTPUT_FILE))

    output_file = open("./{}".format(OUTPUT_FILE), 'w')
    output_file.write("hello world")
    output_file.close()
    print("\n")
