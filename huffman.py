import os


def list_to_str(array):
    text = ""
    for element in array:
        text += element
    return text


if __name__ == '__main__':

    if not os.path.isfile('./input.txt'):
        os.mknod("input.txt")
        raise Exception("Type text to be encoded to input.txt")

    if not os.path.getsize("./input.txt"):
        raise Exception("input.txt is empty")

    input_text = []
    with open('./input.txt') as input_file:
        input_text = input_file.readlines()

    mystring = list_to_str(input_text)
    print(mystring)

    if not os.path.isfile('./output.txt'):
        os.mknod("output.txt")

    output_file = open("./output.txt", 'w')
    output_file.write("hello world")
    output_file.close()
    print("\n")