class Algarismo(object):
    def __init__(self,value) -> None:
        self.value = value

    def getValue(self):
        return self.value

    

if __name__ == "__main__":
    array = []
    vezes = int(input("Quantos algarismos deseja criar: "))

    for x in range(vezes):
        value = input(f'Qual é o valor do {x+1}º algarismo: ')
        array.append(Algarismo(value))

    for x in range(len(array)):
        print(f'O valor do {x+1}º algarismo é: {array[x].getValue()}')