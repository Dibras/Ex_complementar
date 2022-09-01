x = input("Arquivo com a extenção: ")
file = open(x, "r")
lines = file.readlines()
cout = 0
case = -1
for i in lines:
    case += 1
    if i != '\n':
        cout += 1
print("Seu arquivo tem", cout, "linhas")
file.close()