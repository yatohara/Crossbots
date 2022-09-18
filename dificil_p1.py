import re


def diamond_finder(sequence: str) -> int:
    """ Uma função que ira receber uma sequencia de caracteres e retorna quantas vezes aparece "<>"

    Primeiramente é eliminado todos os ".," da sequencia sobrando apenas "<" e ">", com isso é feito um loop que
    conta quantas vezes aparece o "<>" e o elimina, possibilitando a formação de novos "<>". Esse processo é repetido
    até que não haja mais nenhuma padrão "<>"

    :param sequence: uma sequencia dos caracteres: <>.,
    :return: numero de diamantes
    """
    sequence = re.sub(r'[^<>]', '', sequence)  # elimina tudo que não seja "<" ou ">"
    diamonds = 0  # uma variavel que vai receber a quantidade de diamantes

    while re.search(r'<>', sequence):  # enquanto aparecer "<>" o loop é executado

        diamonds += len(re.findall(r'<>', sequence))  # procura todas as aparições de "<>" e a soma com a quantidade
        # de diamantes

        sequence = re.sub(r'<>', '', sequence)  # irá eliminar as sequencias já achadas de "<>"

    return diamonds


for i in range(int(input())):
    print(diamond_finder(input()))

# Casos de teste
if __name__ == '__main__':
    print(diamond_finder('<<<....>>...<,>>..<.....<<...>'))
    print(diamond_finder('<.<>,<.>.<.><<<>'))
