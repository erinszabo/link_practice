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

    def get_data_name(self):
        return self.data.get_name()

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
            lst.append(str(tmp.get_data_name()))
            tmp = tmp.get_next()

            if tmp is not None:
                lst.append(", ")

        lst.append("]")
        return "".join(lst)

    def get_size(self):
        return self.size


def main():
    lst = LinkedList()

    for i in range(5):
        lst.append(Node(Data(str("piece of data"))))

    print(lst)
    print(lst.get_size())
    print(lst.last.get_data())
    print(lst.last.get_data_name())


if __name__ == "__main__":
    main()
    print('done')
