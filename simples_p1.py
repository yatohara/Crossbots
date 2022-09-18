from typing import Union


def soma_posicao(lst: list, x: int, y: int) -> Union[float, None]:
    """ Uma função que irá retornar a soma de dois valores no vet1or

    A função irá calcular a soma do valor associado a posição x no vetor com o valor associado a posição y no vetor,
    caso as posições não estejam no vetor, irá retornar None do contrário retorna a soma


    :param lst: Uma lista/vetor com 10 valores
    :param x: Corresponde a uma posicao em lst
    :param y: Corresponde a outra posicao em lst
    :return: A soma de lst[x] + lst[y] ou None
    """
    # verifica se a posicao passada está dentro do vetor
    if ((x < 0) or (x > 9)) or ((y < 0) or (y > 9)):
        return None

    # retorna a soma dos indices
    return lst[x] + lst[y]


lst_valores = []  # cria a lista dos valores

for i in range(10):
        lst_valores.append(float(input()))  # irá pegar o valor passado pelo usuario

x = int(input("Digite x: "))  # pega a posicao x passada pelo usuario
y = int(input("Digite y: "))  # pega a posicao y passada pelo usuario

print(soma_posicao(lst_valores, x, y))

# Outros casos de teste
if __name__ == "__main__":
    lst = [13, 5, 7, 6, 4, 8, 16, 31, 9, 21]
    print(soma_posicao(lst, 4, 7))
    print(soma_posicao(lst, -1, 9))
    print(soma_posicao(lst, 3, 15))
