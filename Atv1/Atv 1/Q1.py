y = 0
while y == 0:
    x = input("Digite um num inteiro: \n")
    if x.isnumeric():
        NumBin = bin(int(x))
        NumBin = NumBin[2:]
        print(NumBin)
        y = 1
    else:
        print("Digite um valor válido\n")
