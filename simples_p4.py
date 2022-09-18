def encontrar_letra(letter: str, word: str) -> int:
    """ Uma função que irá contar quantas vezes uma letra se repete na palavra passada

    A função built-in do python count() será responsável por fazer isso

    :param letter: A letra procurada na palavra
    :param word: A palavra em que a letra será analisada
    :return: A quantidade de vezes que a letra se repete
    """
    return word.count(letter)


if __name__ == "__main__":
    print(encontrar_letra('a', 'batata'))
    print(encontrar_letra('g', 'cenoura'))
