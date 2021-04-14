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
