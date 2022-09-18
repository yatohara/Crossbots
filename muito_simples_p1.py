import math


def dist(p1: list, p2: list) -> float:
    """Calcula a distância entre dois pontos cartesianos

    É utilizada a fórmula de geometria analítica da distância entre dois pontos

    :param p1: uma lista contendo as coordenadas de um ponto (x, y)
    :param p2: uma lista contendo as coordeandas de outro ponto (x, y)
    :return: a distância entre o ponto p1 e o p2
    """
    qd_dif = lambda x, y, i: pow(x[i] - y[i], 2)
    return round(math.sqrt(qd_dif(p1, p2, 0) + qd_dif(p1, p2, 1)), 5)


# Caso de testes
if __name__ == "__main__":
    print(dist([1, 2], [5, 6]))
