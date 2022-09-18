import math


def angulo(p1: list, p2: list, p3: list) -> float:
    """ Uma função que recebe 3 pontos no plano cartesiano e retorna o angulo em graus entre eles

    Usando conceitos de geometria analitica e algebra linear, o angulo entre os pontos p1, p2 e p3, pode ser calculado
    através do angulo entre o vetor p1p2 e p1p3, tal que o angulo será igual ao arccos = p1.p2/(|p1|*|p2|)

    :param p1: Primeiro ponto (x, y)
    :param p2: Segundo ponto (x, y)
    :param p3: Terceiro ponto (x, y)
    :return:  angulo entre os pontos
    """
    modulo_vetor = lambda x: math.sqrt(pow(x[0], 2) + pow(x[1], 2))  # Gera uma função para calcular o módulo do vetor
    vet_1 = [x - y for x, y in zip(p2, p1)]  # irá calcular o vetor BA
    vet_2 = [x - y for x, y in zip(p2, p3)]  # irá calcular o vetor BC
    intern_product = sum([x * y for x, y in zip(vet_1, vet_2)])  # calcula o produto interno entre os vetores
    angle = math.acos(intern_product / (modulo_vetor(vet_1) * modulo_vetor(vet_2)))  # retorna o angulo em radianos

    return round(angle*360 / (2 * math.pi), 2)  # converte o angulo para graus e o retorna


# Caso de teste
if __name__ == "__main__":
    print(angulo([1, 2], [0, -9], [3, -4]))


