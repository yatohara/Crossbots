def converter_temperatura(temp_fah: float) -> float:
    """ Recebe uma temperatura em graus fahrenheit e a converte para graus celsius

    É utilizada a seguinte fórmula de conversão: (T°F − 32) × 5/9 = T°C

    :param temp_fah: Temperatura em graus fahrenheit
    :return: Temperatura em graus celsius
    """
    return round((temp_fah - 32) * 5/9, 2)


if __name__ == "__main__":
    print(converter_temperatura(77.2))
