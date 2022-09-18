def perfeito(num: int) -> bool:
    """ Verifica se o número é perfeito retornando True ou False

    A funcao ira encontrar os divisores do numero, exceto o próprio numero, e soma-los se a soma for igual o numero
    ele é considerado um numero perfeito e é retornado True

    :param num: um inteiro
    :return: True se for um numero perfeito False se não for um numero perfeito
    """
    # encontra os divisores do numero e os soma
    soma = sum([i for i in range(1, num // 2 + 1) if num % i == 0])

    # verifica se a soma dos divisores é igual ao numero
    if soma == num:
        return True

    return False


if __name__ == "__main__":
    print(perfeito(6))
    print(perfeito(8))
    print(perfeito(28))
