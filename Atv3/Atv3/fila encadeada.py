class N:
    def __init__(self, data):
        self.data = data
        self.next = None

class L:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = N(elem)
        else:
            self.head = N(elem)
        self.size = self.size + 1
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        # a = lista [6]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index of range")
        if pointer:
            return pointer.data
        raise IndexError("list index of range")

    def __setitem__(self, index, elem):
        # lista [6] = 9
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index of range")

    def index(self, elem):
        pointer = self.head
        i = 0
        while (pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem):
        if index == 0:
            node = N(elem)
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            for i in range(index-1):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError("list index of range")  
            node = N(elem)
            node.next = pointer.next
            pointer.next = node
            self.size = self.size + 1 
    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
                self.size = self.size - 1
            return True
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
        r = r [:-3]
        return r
            
    def __str__(self):
        return self.__repr__()


lista = L()

