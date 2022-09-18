def primos(lst_num: list) -> list:
    """ Uma funcao que recebe uma lista de numeros e retorna outra lista com os numeros primos contidos na lista

    Cada numero presente na lista e analisado individualmente para ver se ele é divisível apenas por 1

    :param lst_num: Uma lista de numeros inteiros
    :return: Os numeros primos contidos na lst_num
    """

    lst_primos = []
    for num in lst_num:
        flag = 0  # uma variavel responsavel por armazenar por quantos numeros o numero será divisivel

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                flag += 1

        if flag == 1:  # caso a flag seja igual a 1, significa que o numero é primo
            lst_primos.append(num)

    return lst_primos


# Casos de testes
if __name__ == '__main__':
    lst = [x for x in range(100)]
    print(primos(lst))
