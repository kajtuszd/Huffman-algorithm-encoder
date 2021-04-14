import os

if __name__ == '__main__':

    if not os.path.isfile('./input.txt'):
        os.mknod("input.txt")
        raise Exception("Type text to be encoded to input.txt")

    input_text = []
    with open('./input.txt') as input_file:
        input_text = input_file.readlines()

    print([line for line in input_text])

    if not os.path.isfile('./output.txt'):
        os.mknod("output.txt")

    output_file = open("./output.txt", 'w')
    output_file.write("hello world")
    output_file.close()
    print("\n")