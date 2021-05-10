import os
import zlib
import json
from tree import Tree


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def list_to_str(array):
    text = ""
    for element in array:
        text += element
    return text


def create_directories():
    if not os.path.isfile('./{}'.format(INPUT_FILE)):
        os.mknod("{}".format(INPUT_FILE))
        raise Exception("Type text to be encoded in {}".format(INPUT_FILE))

    if not os.path.getsize("./{}".format(INPUT_FILE)):
        raise Exception("{} is empty".format(INPUT_FILE))

    if not os.path.isfile('./{}'.format(OUTPUT_FILE)):
        os.mknod("{}".format(OUTPUT_FILE))


def read_input():
    input_text = []
    with open('./{}'.format(INPUT_FILE)) as input_file:
        input_text = input_file.readlines()
    # print("Input: {} \n".format(list_to_str(input_text))) # uncomment to see input
    return list_to_str(input_text)


def save_compressed_text(codes, encoded_text):
    output_file = open("./{}".format(OUTPUT_FILE), 'wb')
    # print("Codes: {}\n".format(codes)) # uncomment to see codes dict
    codes = json.dumps(codes)
    codes = bytearray(codes.encode('utf-8'))
    compressed_codes = zlib.compress(codes)
    encoded_text = bytearray(encoded_text.encode('utf-8'))
    compressed = zlib.compress(encoded_text)
    # print("Compressed string: {}\n".format(compressed)) # uncomment to see compressed text
    # print("Compressed codes: {}".format(compressed_codes)) # uncomment to see codes compressed
    output_file.write(compressed)
    output_file.write(compressed_codes)
    output_file.close()


def main():
    create_directories()
    tree = Tree(read_input())
    encoded_text, codes = tree.compute()
    save_compressed_text(codes, encoded_text)


if __name__ == '__main__':
    main()
