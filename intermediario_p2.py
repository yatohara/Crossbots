def nao_repetidos(lst: list) -> list:
    """ Recebe uma lista com numeros repetidos e retorna uma lista sem valores repetidos

    Convertendo a lista para um set(), os valores repetidos são excluidos, já que o set() aceita apenas valores
    distintos, após isso o set() é convertido novamente para uma lista

    :param lst: uma lista com numeros repetidos ou nao
    :return: retorna a lista sem valores repetidos
    """

    return list(set(lst))


# casos de teste
if __name__ == '__main__':
    print(nao_repetidos([1, 4, 5, 13, 10, 10, 9, 8]))




