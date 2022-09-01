class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

def dp(numb):
    st2 = Stack()

    while numb > 0:
        rem = numb % 2
        st2.push(rem)
        numb = numb // 2

    numbin = ""
    while not st2.isEmpty():
        numbin = numbin + str(st2.pop())

    return numbin
x = input("Numero inteiro: ")
print(dp(int(x)))


