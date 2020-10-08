"""


"""


class Data:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def append(self, node):
        if self.size == 0:
            self.first = node
        else:
            self.last.set_next(node)

        self.last = node
        self.size += 1

    def __str__(self):
        lst = ['[']
        tmp = self.first
        while tmp is not None:
            lst.append(str(tmp.get_data()))
            tmp = tmp.get_next()

            if tmp is not None:
                lst.append(", ")

        lst.append("]")
        return "".join(lst)


def main():
    lst = LinkedList()

    for i in range(5):
        lst.append(Node(Data(str(i))))

    print(lst)


if __name__ == "__main__":
    main()