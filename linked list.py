

class NodeList():

    def __init__(self, currentvalue = None, nextelement = None):

        self.value = currentvalue
        self.next = nextelement


class LinkedList():

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):

        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        newnode = NodeList(x, None)
        if self.first is None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = newnode
            self.first = newnode
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = newnode
            self.last = newnode

    def push(self, x):

        if self.first is None:
            newnode = NodeList(x)
            self.first = newnode
            self.last = newnode
        else:
            self.first = NodeList(x, self.first)



l = LinkedList()

l.add(1)
l.add(3)
l.add(4)
l.add(5)
l.push(10)
print(l)