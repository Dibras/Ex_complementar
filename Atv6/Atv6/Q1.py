file = open("arq.txt", "a")
x = ""
while x != "0":
    x = input("Digite para add: ")
    if x != "0":
        file.write(" ")
        file.write(x)
file.close()
file = open("arq.txt", "r") 
print(file.read())
file.close()
