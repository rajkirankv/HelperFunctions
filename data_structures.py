class Stack:
    def __init__(self):
        self.data = list()

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


class Queue:
    def __init__(self):
        self.data = list()

    # Instance methods
    def enqueue(self, element):
        self.data.insert(0, element)
        return

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def is_emtpy(self):
        return self.data == []


class Deque:
    def __init__(self):
        self.data = list()

    def add_front(self, element):
        return self.data.append(element)

    def add_rear(self, element):
        return self.data.insert(0, element)

    def remove_front(self):
        return self.data.pop()

    def remove_rear(self):
        return self.data.pop(0)

    def is_empty(self):
        return self.data == 0

    def size(self):
        return len(self.data)


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_node):
        self.next = new_node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.root = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        if self.head is None:  # The very first node created with always be the root
            self.root = temp
        self.head = temp
        temp = None

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
        return count

    def search(self, item):
        found = False
        temp = self.head
        while temp is not None and not found:
            if item.equals(temp.get_data()):
                found = True
                return found
            else:
                temp = temp.next
        return found

    def remove(self, item):
        temp = self.head
        if temp is None:  # 0 nodes in the list
            return False
        elif temp.get_next() is None:  # 1 node in the list
            if item.equals(temp.get_data()):  # node 1 has the item
                self.head = None
                temp = None
                return True
            else:  # node 1 does NOT have the item
                return False
        elif temp.get_next().get_next() is None:  # the list has 2 nodes in the list
            temp2 = temp.get_next()
            if item.equals(temp.get_data()):  # node 1 has the item
                self.head = temp2
                temp = None
                temp2 = None
                return True
            elif item.equals(temp2.get_data()):  # node 2 has the item
                temp.set_next(None)
                temp = None
                temp2 = None
                return True
            else:  # no node has the item
                temp = None
                temp2 = None
                return False
        else:  # the list has more than 2 nodes
            temp2 = temp.get_next()
            if item.equals(temp.get_data()):  # node 1 has the item
                self.head = temp2
                temp = None
                temp2 = None
                return False
            else:
                while temp2.get_next() is not None and not item.equals(temp2.get_data()):
                    temp = temp2
                    temp2 = temp2.get_next()
                if temp2.get_next() is None:
                    temp = None
                    temp2 = None
                    return False
                else:
                    temp.set_next(temp2.get_next())
                    temp = None
                    temp2 = None
                    return True

    def insert(self, item, position=0):
        if position > self.size():
            raise ValueError("Position out of bounds")
        if position == 0:
            temp = Node(item)
            temp.set_next(self.head)
            self.head = temp
        else:
            temp = self.head
            temp2 = self.head.get_next()
            for i in range(1, position):
                temp = temp2
                temp2 = temp2.get_next()
            temp.set_next(Node(item))
            temp.get_next().set_next(temp2)
            temp = None
            temp2 = None

    def index(self, item):
        position = 0
        temp = self.head
        while temp is not None and not item.equals(temp.get_data()):
            temp = temp.get_next()
            position += 1
        if temp is None:
            raise ValueError('Item not found')
        else:
            return position

    def pop(self, position=0):
        if position > self.size() or position < 0:
            raise ValueError('Position beyond the list size')
        else:
            if position == 0:
                temp = self.head
                self.head = self.head.get_next()
                return temp.get_data()
            else:
                temp = self.head
                temp2 = temp.get_next()
                for i in range(1, position):
                    temp = temp2
                    temp2 = temp2.get_next()
                temp2 = temp2.get_next()
                item = temp.get_next().get_data()
                temp.get_next().set_next(None)
                temp.set_next(temp2)
                return item

    def append(self, item):
        temp = Node(item)
        temp.set_next(None)
        self.root.set_next(temp)
        self.root = temp
